# Main entry point of the application
import argparse
from config import set_debug_mode

from control.control import CentralControlModule
from modules.speech_recognition_io import SpeechRecognitionModule
import threading

def main(debug=False):
    if debug:
        print("Running in debug mode...")

    #TODO: We need to add debugging flags to display debug messages
    if debug:
        print("Starting NeoGlasses v0.1...")
        
    try:
        # Creating an instance of the Central Control Module (Microkernel)
        central_control = CentralControlModule()
        speech_recognition = SpeechRecognitionModule(central_control)
        
        # Enable speech recognition and running it on a separate thread
        if debug:
            key_listener_thread = threading.Thread(target=speech_recognition.start_manual_commands)
            key_listener_thread.start()
        else:
            speech_recognition.enable()
            speech_thread = threading.Thread(target=lambda: speech_recognition.process_command)
            speech_thread.start()

        # Start the main loop of the central control
        # This loop will keep the application running and responsive to module interactions
        central_control.main_loop()

    
    except KeyboardInterrupt:
        # Graceful shutdown if the program is interrupted (e.g., Ctrl+C)
        if debug: print("Shutting down the system...")
        # Here we can add any cleanup or shutdown procedures
    except Exception as e:
        # Handle any unexpected exceptions
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
    main(debug=args.debug)
