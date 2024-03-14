from modules.commands import Commands
from pynput import keyboard


class MockSpeechRecognition:
    def __init__(self, neo, commands):
        self.neo = neo
        self.commands = commands
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
                self.manually_process_command(mode='idle')
            elif key.char == '2':
                self.manually_process_command(mode='find', obj_lbl='cell phone')
            elif key.char == '3':
                self.manually_process_command(mode='read')
            elif key == keyboard.Key.esc:  # Terminate listening when 'esc' is pressed
                self.disable()
        except AttributeError:
            pass  # Non-character keys (e.g., shift, ctrl) are ignored

    def process_command(self):
        self.listener.start()
    
    def manually_process_command(self, mode:str= "idle", obj_lbl:str= ""):
        data ={
                'mode' : None,
                'specific_object_label' : None
            }

        # Get the right command mode
        data['mode'] = self.commands.get_command_mode(mode) 
        # Get the specified object label if it exists
        data['specific_object_label'] = self.commands.get_object_label(obj_lbl)

        if mode:
            self.send_command(data)

    def send_command(self, data: dict):
        self.neo.send_command(data)
