# Main entry point of the application
import argparse
import threading
import queue

from config import set_debug_mode, set_gui_mode

from control.control import CentralControlModule
from control.user_input import UserInputModule
from control.NeoGlassesGUI import NeoGlassesGUI


class NeoGlasses:

    def __init__(self):
        self.command_queue = queue.Queue()
        self.frame_queue = queue.Queue()
        pass

    def send_command(self, data):
        # TODO: call curent_mode.deactivate() from here
        self.command_queue.put(data)

    def main(self, debug=False, gui=False):
        if debug:
            print("Running in debug mode...")
            
        try:
            self.central_control = CentralControlModule(self.command_queue, self.frame_queue)
            self.user_input = UserInputModule(self)
            self.user_input.enable()


            target_function = lambda: self.user_input.process_command()
            command_input_thread = threading.Thread(target=target_function)
            command_input_thread.start()
            
            if gui:
                self.neo_gui = NeoGlassesGUI(self.frame_queue)
                neo_gui_thread = threading.Thread(target=self.neo_gui.mainloop)
                neo_gui_thread.start()

            self.central_control.main_loop()

        
        except KeyboardInterrupt:
            # Graceful shutdown if the program is interrupted (e.g., Ctrl+C)
            if debug: print("Shutting down the system...")
        except Exception as e:
            if debug: print(f"An unexpected error occurred: {e}")
        finally:
            # Any final cleanup code can be placed here
            # This is important for releasing resources like file handles or network connections
            # self.user_input.disable()
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the central control system.')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode for verbose output')
    parser.add_argument('--gui', action='store_true', help='Enable GUI mode for visual output')
    args = parser.parse_args()

    # Set the debug and gui mode in the config
    set_debug_mode(args.debug)
    set_gui_mode(args.gui)


    # Call main with the debug argument
    neo = NeoGlasses()
    neo.main(debug=args.debug, gui=args.gui)
