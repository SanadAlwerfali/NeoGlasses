from modes.mode import Mode

class TextReadingMode(Mode):
    def __init__(self, control_module):
        super().__init__()
        
        self.control_module = control_module

    def activate(self):
        # Enable necessary modules for text reading
        self.control_module.io_modules['camera'].enable()
        self.control_module.modules['text_recognition'].enable()

    def deactivate(self):
        # Disable the modules when leaving text reading mode
        self.control_module.io_modules['camera'].disable()
        self.control_module.modules['text_recognition'].disable()

    def __name__(self):
        return "TextReading"