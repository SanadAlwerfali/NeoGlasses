from modes.mode import Mode
from time import sleep

class TextReadingMode(Mode):
    def __init__(self, control_module):
        super().__init__()
        self.control_module = control_module

    def activate(self):
        self.isActive = True
        # Enable necessary modules for text reading
        self.control_module.io_modules['camera'].enable()
        self.control_module.modules['text_recognition'].enable()
        self.control_module.modules['text_to_speech'].enable()

    def deactivate(self):
        self.isActive = False
        # Disable the modules when leaving text reading mode
        self.control_module.io_modules['camera'].disable()
        self.control_module.modules['text_recognition'].disable()
        self.control_module.modules['text_to_speech'].disable()

    def main_loop(self):
        while self.isActive:
            #write the logic here
            text_from_camera = "This is a placeholder value for the text from camera"
            self.control_module.modules['text_to_speech'].convert(text_from_camera)
            pass

    def __name__(self):
        return "TextReading"