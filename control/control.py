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
from modules.text_recognition_io import TextRecognitionModule
from modules.object_detection_io import ObjectDetectionModule
# importing other modules
from time import sleep
from config import is_debug_mode


class CentralControlModule:
    
    def __init__(self, command_queue, frame_queue, yolo):
        self.isAlive = True
        
        self.command_queue = command_queue
        self.frame_queue = frame_queue
        # Initialize io_modules
        self.io_modules = {
            'camera': CameraModule(),
            'speaker': SpeakerModule(),
            'microphone': MicrophoneModule(),
        }
        # Initialize odules
        self.modules = {
            'text_recognition': TextRecognitionModule(),
            'object_detection': ObjectDetectionModule(),
        }
        # Initialize modes
        self.modes = {
            'TextReading': TextReadingMode(camera=self.io_modules['camera'], speaker=self.io_modules['speaker'], frame_queue=frame_queue),
            'ObjectFinding': ObjectFindingMode(camera=self.io_modules['camera'], speaker=self.io_modules['speaker'], frame_queue=frame_queue, yolo=yolo),
            'Idle': IdleMode(speaker=self.io_modules['speaker']),
        }

        # Initialize current_mode and pass shared objects among the modes

        self.current_mode = self.modes['Idle']
        if is_debug_mode(): print(f"Central Control Module initialized.\nCurrent mode: {self.current_mode.__name__()}")

    def switch_mode(self, data):
        cmmnd_mode_name = data['mode']

        # Deactivate current mode
        if self.current_mode:
            self.current_mode.deactivate()

        try:
            if is_debug_mode(): print(f"Switching to mode: {cmmnd_mode_name}")
            # Get mode
            self.current_mode = self.modes.get(cmmnd_mode_name)
            # Activate new mode
            self.current_mode.activate(target_label=data['specific_object_label']) 

        except Exception as e:
            self.current_mode = self.modes['Idle']
            if is_debug_mode(): 
                print(f"Caught exception while activating Mode {cmmnd_mode_name}.")
                print(e)
                print(f"Switching to mode: {self.current_mode.__name__()}")
            self.current_mode.activate()


    def receive_command(self, data: dict):
        if 'hey neo' in data: #FIXME
            # TODO: play a ding sound
            self.switch_mode('Idle')

        if 'mode' in data and data['mode'] in self.modes:
            self.switch_mode(data)

        else:
            if is_debug_mode(): print(f"Received notification with data: {data}")

    def main_loop(self):
        # Main loop logic

        while self.isAlive:
            sleep(2)
            print("checking queue")

            if not self.command_queue.empty():
                data = self.command_queue.get()
                self.receive_command(data)

            #FIXME: Need to override current_mode main_loop incase of New Mode called
            # Maybe let it run in a separate thread?
            self.current_mode.main_loop()

    def deactivate(self):
        self.isAlive = False
        self.current_mode.deactivate()
        for io_module in self.io_modules.values():
            io_module.disable()

    def __name__(self):
        return "Central Control Module"