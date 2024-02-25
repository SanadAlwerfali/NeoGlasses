# Text-to-Speech Module
from modules.module__io import ModuleIO

class TextToSpeechModule(ModuleIO):
    def __init__(self, module):
        # Initialize text-to-speech parameters
        super().__init__()
        self.speaker = module.io_modules['speaker']

    def convert_text_to_speech(self, text):
        print("converting text to speech: ", text)
        if self.isEnabled:
            # Logic to get rid of weird characters in text
            self.speaker.say(text)
            pass

    def enable(self):
        # Enable text-to-speech
        self.isEnabled = True

    def disable(self):
        # Disable text-to-speech
        self.isEnabled = False

    def __name__(self) -> str:
        return "TextToSpeech"