# Text-to-Speech Module
from modules.module__io import ModuleIO

class TextToSpeechModule(ModuleIO):
    def __init__(self):
        # Initialize text-to-speech parameters
        super().__init__()

    def convert_text_to_speech(self, text):
        if self.isEnabled:
            # Text-to-speech logic
            # May include notifying the control module when speech is done
            pass

    def enable(self):
        # Enable text-to-speech
        self.isEnabled = True

    def disable(self):
        # Disable text-to-speech
        self.isEnabled = False

    def __name__(self) -> str:
        return "TextToSpeech"