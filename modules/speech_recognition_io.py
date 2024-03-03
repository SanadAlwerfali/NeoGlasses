from modules.commands import Commands
from io_modules.microphone import MicrophoneModule
from playsound import playsound


class SpeechRecognition:
    def __init__(self, neo):
        self.neo = neo
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
                    data = {"mode": "", "text": ""}
                    # Voice command processing logic
                    new_mode = Commands.get_command_mode(text)  # get the right command mode
                    data["mode"] = new_mode
                    data["text"] = (
                        text  # TODO: get the needed text from the argument passed
                    )

                    if new_mode:
                        print(new_mode)
                        self.send_command(data)

    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False

    def send_command(self, data: dict):
        if not data:
            data = dict()
        self.neo.send_command(data)
