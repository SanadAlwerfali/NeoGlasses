
from modules.commands import Commands

class SpeechRecognition:

    def process_command(self):
        text = ""
        # Process voice command
        #TODO: Add a listen() to continuously listening to voice commands from Kareems
        if self.isEnabled:
            data ={
                'mode' : None,
                'text' : None
            }
            # Voice command processing logic
            new_mode = Commands.get_command_mode(text) # get the right command mode
            data['mode'] = new_mode
            data['text'] = text # TODO: get the needed text from the argument passed

            if new_mode:
                self.send_command(data)
    
    def __init__(self, neo):
        self.neo = neo
    
    def enable(self):
        self.isEnabled = True        

    def disable(self):
        self.isEnabled = False

    def send_command(self, data: dict):
        self.neo.send_command(data)