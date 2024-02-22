# Central Control Module

# importing io_modules
from io_modules.camera import CameraModule
from io_modules.speaker import SpeakerModule
from io_modules.microphone import MicrophoneModule
# importing modes
from modes.mode import Mode
from modes.idle_mode import IdleMode
from modes.text_reading_mode import TextReadingMode
from modes.object_finding_mode import ObjectFindingMode
# importing modules
from utils.text_recognition import TextRecognition
from utils.object_detection import ObjectDetection
# importing other modules
from time import sleep
from config import is_debug_mode


class CentralControl:
    current_mode = Mode()
    
    def __init__(self):
        
        # Initialize io_modules
        self.io_modules = {
            'camera': CameraModule(self, ),
            'speaker': SpeakerModule(self),
            'microphone': MicrophoneModule(self),
        }

        # Initialize modes
        self.modes = {
            'TextReading': TextReadingMode(self),
            'ObjectFinding': ObjectFindingMode(self),
            'Idle': IdleMode(self),
        }

        # Initialize odules
        self.modules = {
            'text_recognition': TextRecognition(),
            'object_detection': ObjectDetection(),
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
        if 'hey neo' is in command:
            # TODO: play a ding sound
            self.switch_mode('Idle')

        if 'mode' in data and data['mode'] in self.modes:
            self.switch_mode(data['mode'])

        else:
            if is_debug_mode(): print(f"Received notification with data: {data}")

    def main_loop(self):
        # Main loop logic

        while True:
            sleep(2)
            
            if not self.command_queue.empty():
                data = self.command_queue.get()
                receive_command(data)

            self.current_mode.main_loop()


