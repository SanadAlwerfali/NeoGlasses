import subprocess
import pyttsx3

class SpeakerModule:
    def __init__(self, control_module):
        self.control_module = control_module
        self.enabled = False
        self.engine = pyttsx3.init()
        self.rate = 150  # Arbitrary constant value of 150 based on testing

    def enable(self):
        self.enabled = True
        self.engine.setProperty('rate', self.rate)
        self.engine.setProperty('voice', 'com.apple.voice.compact.en-US.Samantha')

    def speak(self, text):
        if not self.enabled:
            print("Speaker is not enabled. Call 'enable()' to start speaking.")
            return
        self.engine.say(text)
        self.engine.runAndWait()
        
    def interrupt(self):
        self.engine.stop()
    
    def disable(self):
        self.interrupt()
