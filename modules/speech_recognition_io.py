# Voice Command Processing Module
from modules.commands import Commands
from modules.module__io import ModuleIO

# Modules for deugging/testing purposes
from config import is_debug_mode
from pynput import keyboard

class SpeechRecognitionModule(ModuleIO):
    def __init__(self, neo):
        if not is_debug_mode():
            self.impl = SpeechRecognition(neo)
        else:
            self.impl = MockSpeechRecognition(neo)

    def process_command(self, mode:str= "Idle"):
        self.impl.process_command(mode)

    def enable(self):
        self.impl.enable()

    def disable(self):
        self.impl.disable()

    def send_command(self, data: dict):
        self.impl.send_command(data)

    def __name__(self) -> str:
        return "SpeechRecognition"
    


class SpeechRecognition:

    def process_command(self, mode:str= "Idle"):
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


class MockSpeechRecognition:
    def __init__(self, neo):
        self.neo = neo
        self.listener = None

    def enable(self):
        self.isEnabled = True
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        print("Manual commands started.")

    def disable(self):
        self.isEnabled = False
        if self.listener:
            self.listener.stop()

        print("Manual commands stopped.")

    def on_press(self, key):
        try:
            if key.char == '1':
                self.manually_process_command(mode='Idle')
            elif key.char == '2':
                self.manually_process_command(mode='ObjectFinding')
            elif key.char == '3':
                self.manually_process_command(mode='TextReading')
            elif key == keyboard.Key.esc:  # Terminate listening when 'esc' is pressed
                self.stop_manual_commands()
        except AttributeError:
            pass  # Non-character keys (e.g., shift, ctrl) are ignored

    def process_command(self, mode:str= "Idle"):
        data = {
            'mode' : str,
            'text' : str
        }
        data['mode'] = mode
        data['text'] = "dummy data"

        if mode:
            self.send_command(data)

    def send_command(self, data: dict):
        self.neo.send_command(data)
