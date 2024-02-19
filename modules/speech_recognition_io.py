# Voice Command Processing Module
from modules.commands import Commands
from control.control import CentralControlModule
from modules.module__io import ModuleIO

# Modules for deugging/testing purposes
from config import is_debug_mode
from pynput import keyboard

class SpeechRecognitionModule(ModuleIO):
    def __init__(self, control_module: CentralControlModule):
        # Initialize speech recognition parameters
        super().__init__()
        self.control_module = control_module
        if is_debug_mode(): 
            self.listener = None
            print("Speech recognition module initialized")


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
                self.send_notification(self.__name__(), data)


    def send_notification(self, module_name, data: dict):
        self.control_module.receive_notification(module_name, data)

    def enable(self):
        # Enable speech recognition
        self.isEnabled = True

    def disable(self):
        # Disable speech recognition
        self.isEnabled = False

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

    def start_manual_commands(self):
        if is_debug_mode():
            # Starting the listener in a non-blocking fashion
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            print("Manual commands started.")

    # Testing functions
    def manually_process_command(self, mode:str= "Idle"):
        data = {
            'mode' : str,
            'text' : str
        }
        data['mode'] = mode
        data['text'] = "dummy data"

        if mode:
            self.send_notification(self.__name__(), data)

    def stop_manual_commands(self):
        if self.listener:
            self.listener.stop()
            print("Manual commands stopped.")


    def __name__(self) -> str:
        return "SpeechRecognition"
    