# Main entry point of the application
import argparse
import threading
import queue

from config import set_debug_mode

from control.control import CentralControlModule
from modules.speech_recognition_io import SpeechRecognitionModule


class NeoGlasses:

    def __init__(self):
        self.command_queue = queue.Queue()
        pass

    def send_command(self, data):
        # TODO: call curent_mode.deactivate() from here
        self.command_queue.put(data)

    def main(self, debug=False):
        if debug:
            print("Running in debug mode...")
            
        try:
            self.central_control = CentralControlModule(self.command_queue)
            self.speech_recognition = SpeechRecognitionModule(self)
            self.speech_recognition.enable()

            target_function = lambda: self.speech_recognition.process_command()
            command_input_thread = threading.Thread(target=target_function)
            command_input_thread.start()

            self.central_control.main_loop()

        
        except KeyboardInterrupt:
            # Graceful shutdown if the program is interrupted (e.g., Ctrl+C)
            if debug: print("Shutting down the system...")
        except Exception as e:
            if debug: print(f"An unexpected error occurred: {e}")
        finally:
            # Any final cleanup code can be placed here
            # This is important for releasing resources like file handles or network connections
            self.speech_recognition.disable()
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
