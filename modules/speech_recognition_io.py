from modules.commands import Commands
from playsound import playsound


class SpeechRecognition:
    def __init__(self, neo, commands, microphone):
        self.neo = neo
        self.isEnabled = True
        self.microphone = microphone
        self.commands = commands
        self.microphone.enable()

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
                    new_mode = self.commands.get_command_mode(text)  # get the right command mode
                    data["mode"] = new_mode
                    data["specific_object_label"] = self.commands.get_object_label(text)

                    if data['mode'] is not None:
                         print(f"sending command to switch to {data['mode']}")
                         self.send_command(data)

    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False

    def send_command(self, data: dict):
        if not data:
            data = dict()
        self.neo.send_command(data)
