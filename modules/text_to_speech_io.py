# Text-to-Speech Module
from modules.module__io import ModuleIO
from io_hardware.speaker import SpeakerModule
from time import sleep


class TextToSpeechModule(ModuleIO):
    def __init__(self, microphone=None):
        # Initialize text-to-speech parameters
        super().__init__()
        self.speaker = SpeakerModule()
        self.enable()

    def convert(self, text):
        if self.isEnabled:
            # Text-to-speech logic
            # May include notifying the control module when speech is done
            # Any post processing on the text can be done in a helper function here
            self.speaker.speak(text)
            pass

    def enable(self):
        # Enable text-to-speech
        self.isEnabled = True
        self.speaker.enable()

    def disable(self):
        # Disable text-to-speech
        self.isEnabled = False
        self.speaker.disable()

    def __name__(self) -> str:
        return "TextToSpeech"