
from modules.commands import Commands

class SpeechRecognition:
    def __init__(self, neo, commands):
        self.neo = neo
        self.commands = commands
        
    def process_command(self):
        # Process voice command
        microphone_text = ""
        
        #TODO: Add a listen() to continuously listening to voice commands from Kareems

        if self.isEnabled:
            data ={
                'mode' : None,
                'specific_object_label' : None
            }
            # Voice command processing logic
            
            # Get the right command mode
            data['mode'] = self.commands.get_command_mode(microphone_text) 
            # Get the specified object label if it exists
            data['specific_object_label'] = self.commands.get_object_label(microphone_text)

            if data['mode']:
                self.send_command(data)
    

    
    def enable(self):
        self.isEnabled = True        

    def disable(self):
        self.isEnabled = False

    def send_command(self, data: dict):
        self.neo.send_command(data)