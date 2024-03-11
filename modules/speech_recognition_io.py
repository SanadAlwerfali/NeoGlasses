from modules.commands import Commands
from playsound import playsound
from modules.text_to_speech_io import TextToSpeechModule
import random


class SpeechRecognition:
    def __init__(self, neo, commands, microphone):
        self.neo = neo
        self.commands = commands
        self.isEnabled = True
        self.microphone = microphone
        self.microphone.enable()

        self.cant_understand_audio = ["Sorry, I couldn't understand", "Sorry, command not recognized."]
        self.text_to_speech = TextToSpeechModule(microphone=self.microphone)

        self.wakeup_calls = {'hey neo', 'hey you', 'hello neo', 'okay neo', 'hey neil', 'hello neil', 'okay neil', 'hey new', 'hello new', 'okay new',
                            'daniel', 'tennille', "danielle", "pineal", "continue", "neo", "neil", "nail", "ennio"}

    def process_command(self):
        i = 0
        while self.isEnabled:
            # if not self.microphone.isEnabled:
            #     self.microphone.enable()
            # Process voice command
            print(f"{i}")
            text = "/"
            text = self.microphone.listen()
            if text is not None:
                # self.microphone.disable() # Must Disable so it doesn't pick up its own voice
                if str(self.wakeup_calls).find(text):
                    # try:
                    #     playsound('utils/notifi.wav')
                    # except Exception as e:
                    #     print(e)
                    # print("Waking up Neo!")
                    i=+1
                    data = {"mode": "", "specific_object_label": ""}
                    # Voice command processing logic
                    # Get the right command mode
                    data["mode"] = self.commands.get_command_mode(text) 
                    # Get the specified object label if it exists
                    data["specific_object_label"] = self.commands.get_object_label(text)
                    
                    if data['mode'] is not None:
                        print(data['mode'])
                        self.send_command(data)
                    else:
                        self.text_to_speech.convert(random.choice(self.cant_understand_audio))
                        self.send_command(data)


    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False

    def send_command(self, data: dict):
        if not data:
            data = dict()
        self.neo.send_command(data)
