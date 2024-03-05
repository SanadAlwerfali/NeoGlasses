from modules.commands import Commands
from io_modules.microphone import MicrophoneModule
from playsound import playsound


class SpeechRecognition:
    def __init__(self, neo, commands):
        self.neo = neo
        self.commands = commands
        self.isEnabled = True
        self.microphone = MicrophoneModule()

    def process_command(self):
        text = ""
        # Process voice command
        while True:
            text = self.microphone.listen()
            wakeup_calls = {'hey neo', 'hello neo', 'okay neo', 'hey neil', 'hello neil', 'okay neil', 'hey new', 'hello new', 'okay new', 
                        'daniel', 'tennille', "danielle", "pineal", "continue", "neo", "neil", "nail"}
            
            if text is not None:     
                if text in wakeup_calls:
                    playsound('utils/notification.wav')             
                if self.isEnabled and text:
                    data = {"mode": "", "specific_object_label": ""}
                    # Voice command processing logic
                    # Get the right command mode
                    data["mode"] = self.commands.get_command_mode(text) 
                    # Get the specified object label if it exists
                    data["specific_object_label"] = self.commands.get_object_label(text)

                    if data['mode']:
                        print(data['mode'])
                        self.send_command(data)

    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False

    def send_command(self, data: dict):
        if not data:
            data = dict()
        self.neo.send_command(data)
