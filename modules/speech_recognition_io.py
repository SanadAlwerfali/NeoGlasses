from modules.commands import Commands
from io_modules.microphone import MicrophoneModule
import speech_recognition as sr


class SpeechRecognition:
    def __init__(self, neo):
        self.neo = neo
        self.isEnabled = True

    def process_command(self):
        text = ""
        # Process voice command
        while True:
            text = self.listen()
            if self.isEnabled:
                data = {"mode": "", "text": ""}
                # Voice command processing logic
                new_mode = Commands.get_command_mode(text)  # get the right command mode
                data["mode"] = new_mode
                data["text"] = (
                    text  # TODO: get the needed text from the argument passed ** Kareem: don't get this todo
                )

                if new_mode:
                    print(new_mode)
                    self.send_command(data)

    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False

    def send_command(self, data: dict):
        self.neo.send_command(data)
