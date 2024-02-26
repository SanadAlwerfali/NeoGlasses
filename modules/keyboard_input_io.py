from modules.commands import Commands
from pynput import keyboard
from time import sleep

class MockSpeechRecognition:
    def __init__(self, neo):
        self.neo = neo
        self.listener = None

    def enable(self):
        self.isEnabled = True
        self.listener = keyboard.Listener(on_press=self.on_press)
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
                self.disable()
        except AttributeError:
            pass  # Non-character keys (e.g., shift, ctrl) are ignored

    def process_command(self):
        self.listener.start()
    
    def manually_process_command(self, mode:str= "Idle"):
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
