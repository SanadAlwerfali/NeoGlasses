# Central Control Module

# importing io_modules
import cv2
import numpy as np
import easygui
from io_modules.camera import CameraModule
from io_modules.speaker import SpeakerModule
from io_modules.microphone import MicrophoneModule
# importing modes
from modes.mode import Mode
from modes.idle_mode import IdleMode
from modes.text_reading_mode import TextReadingMode
from modes.object_finding_mode import ObjectFindingMode
# importing modules
from modules.text_recognition_io import TextRecognitionModule
from modules.object_detection_io import ObjectDetectionModule
from modules.text_to_speech_io import TextToSpeechModule
# importing other modules
from time import sleep
from config import is_debug_mode



class CentralControlModule:
    current_mode = Mode()
    
    def __init__(self, command_queue, frame_queue):
        
        self.command_queue = command_queue
        self.frame_queue = frame_queue
        # Initialize io_modules
        self.io_modules = {
            'camera': CameraModule(self),
            'speaker': SpeakerModule(self),
            'microphone': MicrophoneModule(self),
        }
        # Initialize odules
        self.modules = {
            'text_recognition': TextRecognitionModule(),
            'object_detection': ObjectDetectionModule(),
            'text_to_speech': TextToSpeechModule(),
        }
        # Initialize modes
        self.modes = {
            'TextReading': TextReadingMode(self.frame_queue),
            'ObjectFinding': ObjectFindingMode(self.frame_queue),
            'Idle': IdleMode(self.frame_queue),
        }


        # Set initial mode
        self.current_mode = self.modes['Idle']
        if is_debug_mode(): print("Central Control Module initialized.")

    def switch_mode(self, mode_name):
        # Deactivate current mode
        if self.current_mode:
            self.current_mode.deactivate()

        # Activate new mode
        self.current_mode = self.modes.get(mode_name)
        if self.current_mode: # Check if mode exists
            if is_debug_mode(): print(f"Switching to mode: {mode_name}")
            self.current_mode.activate()
        else:
            if is_debug_mode(): print(f"Mode {mode_name} not found.")
            self.switch_mode('Idle')


    def receive_command(self, data: dict):
        if "mode" in data and data["mode"] in self.modes:
            self.switch_mode(data["mode"])

        else:
            if is_debug_mode(): print(f"Received notification with data: {data}")


    def update_status_popup(self):
        status_text = (
            f"Current Mode: {self.current_mode.get_name()}\n" 
            f"{self.current_mode.get_name()} Status: {'On' if self.current_mode.isActive else 'Off'}\n"
            f"Microphone Status: {self.io_modules['microphone'].isEnabled}\n"
            f"Camera Status: {self.io_modules['camera'].isEnabled}\n"
            f"Speaker Status: {self.io_modules['speaker'].isEnabled}"
        )
        #print (status_text)
        easygui.msgbox(status_text, title="System Status", ok_button="OK")

    
    def main_loop(self):
        # Main loop logic
        while True:
            sleep(1)
            # print("checking queue")
            if not self.command_queue.empty():
                data = self.command_queue.get()
                self.receive_command(data)

            self.current_mode.main_loop()
            self.update_status_popup()