import pyttsx3
class SpeakerModule:

    def onStartWord(self, name, location, length):
        if (self.interrupt_val):
            self.engine.stop()
    
    def enable(self):
        self.engine = pyttsx3.init()
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate-35)
        self.engine.setProperty('voice', 'com.apple.voice.compact.en-US.Samantha')
        self.engine.connect('started-word', self.onStartWord) #Subscribe to the started word event

    def __init__(self, control_module, speaker_index=0):
        self.control_module = control_module
        self.speaker_index = speaker_index

    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()

    def setVolume(self, new_volume):
        self.engine.setProperty('volume', new_volume)

    def interrupt(self):
        self.interrupt_val = True

    def disable(self):
        self.engine.stop()
        
