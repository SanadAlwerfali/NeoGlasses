# Text-to-Speech Module
from modules.module__io import ModuleIO
from io_hardware.speaker import SpeakerModule
from time import sleep
import threading

class TextToSpeechModule(ModuleIO):
    SEM = threading.Semaphore(1)
    def __init__(self, microphone=None):
        # Initialize text-to-speech parameters
        super().__init__()
        self.speaker = SpeakerModule()
        self.enable()
        self.microphone = microphone

    def convert(self, text):
        if self.isEnabled:
            TextToSpeechModule.SEM.acquire()
            self.microphone.disable()
            if not self.microphone.isEnabled:
            # Text-to-speech logic
            # May include notifying the control module when speech is done
            # Any post processing on the text can be done in a helper function here
                print(f"Speaking: {text}")
                self.speaker.speak(text)
                # sleep(2)

            self.microphone.enable()
            TextToSpeechModule.SEM.release()

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