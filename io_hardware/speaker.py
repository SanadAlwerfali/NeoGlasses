import subprocess
import pyttsx3

class SpeakerModule:
    def __init__(self):
        self.enabled = True
        self.engine = pyttsx3.init()
        self.rate = 150  # Arbitrary constant value of 150 based on testing

    def enable(self):
        self.enabled = True
        self.engine.setProperty('voice', 'com.apple.voice.compact.en-US.Samantha')
        self.engine.setProperty('rate', self.rate)

    def speak(self, text):
        if not self.enabled:
            raise Exception("Speaker is not enabled. Call 'enable()' to start speaking.")

        self.engine.say(text)
        self.engine.runAndWait()
        
    def interrupt(self):
        self.engine.stop()
    
    def disable(self):
        self.interrupt()
        self.enabled = False
