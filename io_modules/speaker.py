import pyttsx3;

class SpeakerModule:
    engine = None
    interrupt_val = False

    def onStartWord(self, name, location, length):
        global interrupt_val
        print ("interrupt value= ", interrupt_val)
        if (interrupt_val):
            self.engine.stop()

    def __init__(self, control_module, speaker_index=0):
        self.control_module = control_module
        self.speaker_index = speaker_index
        
        self.engine = pyttsx3.init()
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate-35)
        self.engine.setProperty('voice', 'com.apple.voice.compact.en-US.Samantha')
        self.engine.connect('started-word', self.onStartWord) #Subscribe to the started word event

    def speak(self,text):
        print("this is working")
        self.engine.say(text)
        self.engine.runAndWait()

    def increaseVolume(self, new_volume):
        self.engine.setProperty('volume', new_volume)

    def interrupt():
        global interrupt_val
        interrupt_val = True