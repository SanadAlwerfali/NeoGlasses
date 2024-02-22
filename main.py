# Main entry point of the application
import argparse
from config import set_debug_mode

from control.control import CentralControlModule
from modules.speech_recognition_io import SpeechRecognitionModule
import threading

class NeoGlasses:

    def __init__(self):
        pass

    def send_command(self, data):
        self.central_control.receive_notification(data)

    def main(self, debug=False):
        if debug:
            print("Running in debug mode...")

        if debug:
            print("Starting NeoGlasses v0.1...")
            
        try:
            self.central_control = CentralControlModule()
            self.speech_recognition = SpeechRecognitionModule(self)
            
            if debug:
                key_listener_thread = threading.Thread(target=self.speech_recognition.start_manual_commands)
                key_listener_thread.start()
            else:
                self.speech_recognition.enable()
                speech_thread = threading.Thread(target=lambda: self.speech_recognition.process_command)
                speech_thread.start()

            self.central_control.main_loop()

        
        except KeyboardInterrupt:
            # Graceful shutdown if the program is interrupted (e.g., Ctrl+C)
            if debug: print("Shutting down the system...")
        except Exception as e:
            if debug: print(f"An unexpected error occurred: {e}")
        finally:
            # Any final cleanup code can be placed here
            # This is important for releasing resources like file handles or network connections
            if debug:
                speech_recognition.stop_manual_commands()
            speech_recognition.disable()
            pass

    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Run the central control system.')
        parser.add_argument('--debug', action='store_true', help='Enable debug mode for verbose output')
        args = parser.parse_args()

        # Set the debug mode in the config
        set_debug_mode(args.debug)


        # Call main with the debug argument
        neo = NeoGlasses()
        neo.main(debug=args.debug)
