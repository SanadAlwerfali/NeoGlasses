# Voice Command Processing Module
from modules.commands import Commands
from control.control import CentralControlModule
from modules.module__io import ModuleIO

class SpeechRecognitionModule(ModuleIO):
    def __init__(self, control_module: CentralControlModule):
        # Initialize speech recognition parameters
        super().__init__()
        self.control_module = control_module

    def process_command(self, text: str):
        # Process voice command
        #TODO: Add a listen() to continuously listening to voice commands from Kareems
        data ={
            'mode' : None,
            'text' : None
        }
        if self.isEnabled:
            # Voice command processing logic
            new_mode = Commands.get_command_mode(text) # get the right command mode
            data['mode'] = new_mode
            if new_mode != "Idle":
                data['text'] = text # TODO: get the needed text from the argument passed
                self.control_module.receive_notification(self.__name__(), data)
            else:
                self.control_module.receive_notification(self.__name__(), data)

    def enable(self):
        # Enable speech recognition
        self.isEnabled = True

    def disable(self):
        # Disable speech recognition
        self.isEnabled = False

    def __name__(self) -> str:
        return "SpeechRecognition"