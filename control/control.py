# Central Control Module

# importing io_hardware
from io_hardware.camera import CameraModule
from io_hardware.speaker import SpeakerModule
from io_hardware.microphone import MicrophoneModule
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

    def __init__(self, command_queue, frame_queue, yolo, microphone):
        self.isAlive = True
        
        self.command_queue = command_queue
        self.frame_queue = frame_queue
        # Initialize io_hardware
        self.io_hardware = {
            'camera': CameraModule(),
            'speaker': SpeakerModule(),
            'microphone': microphone,
        }
        # Initialize Modules
        self.modules = {
            'text_to_speech': TextToSpeechModule(microphone),
            'object_detection': ObjectDetectionModule(),
        }
        # Initialize modes
        self.modes = {
            'TextReading': TextReadingMode(camera=self.io_hardware['camera'], speaker=self.io_hardware['speaker'], frame_queue=frame_queue, text_to_speech=self.modules['text_to_speech']),
            'ObjectFinding': ObjectFindingMode(camera=self.io_hardware['camera'], speaker=self.io_hardware['speaker'], frame_queue=frame_queue, yolo=yolo, text_to_speech=self.modules['text_to_speech']),
            'Idle': IdleMode(speaker=self.io_hardware['speaker']),
        }

        # Initialize current_mode and pass shared objects among the modes
        self.current_mode = self.modes['Idle']
        if is_debug_mode(): print(f"Central Control Module initialized.\nCurrent mode: {self.current_mode.__name__()}")


    def switch_mode(self, data):
        mode_name = data['mode']
        # Deactivate current mode
        if self.current_mode:
            self.current_mode.deactivate()

        # Activate new mode
        try:
            if is_debug_mode(): print(f"Switching to mode: {mode_name}")
            # Get mode
            self.current_mode = self.modes.get(mode_name)
            # Activate new mode
            self.current_mode.activate(target_label=data['specific_object_label']) 

        except Exception as e:
            self.current_mode = self.modes['Idle']
            if is_debug_mode(): 
                print(f"Caught exception while activating Mode {mode_name}.\n{e}")
                print(f"Switching to mode: {self.current_mode.__name__()}")
            self.current_mode.activate()

    def receive_command(self, data: dict):
        if "mode" in data: #and data["mode"] in self.modes:
            self.switch_mode(data)

        else:
            if is_debug_mode(): print(f"Received notification with data: {data}")

    def main_loop(self):
        # Main loop logic

        while self.isAlive:
            sleep(1)
            # print("checking queue")
            if not self.command_queue.empty():
                data = self.command_queue.get()
                self.receive_command(data)

            self.current_mode.main_loop() # FIXME: Once gets to a loop wont be able to get to intercept the next command

    def deactivate(self):
        self.isAlive = False
        self.current_mode.deactivate()
        for io_module in self.io_hardware.values():
            io_module.disable()

    def __name__(self):
        return "Central Control Module"