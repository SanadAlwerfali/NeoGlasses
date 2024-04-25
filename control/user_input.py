# Voice Command Processing Module
from modules.commands import Commands
from modules.module__io import ModuleIO

from modules.speech_recognition_io import SpeechRecognition
from modules.keyboard_input_io import MockSpeechRecognition

# Modules for deugging/testing purposes
from config import is_debug_mode

class UserInputModule(ModuleIO):
    def __init__(self, neo, commands, microphone):
        # if is_debug_mode():
        #     self.impl = MockSpeechRecognition(neo, commands=commands)
        # else:
        #     self.impl = SpeechRecognition(neo, commands=commands)

        self.impl = SpeechRecognition(neo, commands=commands, microphone=microphone)

    def process_command(self):
        self.impl.process_command()

    def enable(self):
        self.impl.enable()

    def disable(self):
        self.impl.disable()

    def send_command(self, data: dict):
        self.impl.send_command(data)

    def __name__(self) -> str:
        return "SpeechRecognition"
