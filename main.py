# Main entry point of the application
import argparse
import threading
import queue

from config import set_debug_mode, set_gui_mode

from control.control import CentralControlModule
from control.user_input import UserInputModule
from control.NeoGlassesGUI import NeoGlassesGUI

from modules.commands import Commands
from modules.YOLO import YOLO

class NeoGlasses:

    def __init__(self):
        self.central_control = None
        self.user_input = None
        self.neo_gui = None

        self.yolo = None 

        self.command_queue = queue.Queue() # For User Input 
        self.frame_queue = queue.Queue() # For Camera Frames - between Camera(Input) and GUI(Output)

    def send_command(self, data):
        # TODO: call curent_mode.deactivate() from here
        self.command_queue.put(data)

    def main(self, debug=False, gui=False):
        if debug:
            print("Running in debug mode...")
            
        try:
            # Need to initialize yolo at the start of the program
            yoloConfig = 'utilities/yolov3.cfg'
            yoloWeights = 'utilities/yolov3.weights'
            classFile = 'utilities/coco.names'

            yolo = YOLO(yoloConfig, yoloWeights, classFile)

            self.central_control = CentralControlModule(self.command_queue, self.frame_queue, yolo=yolo)
            
            commands = Commands(yolo=yolo)
            self.user_input = UserInputModule(self, commands)
            self.user_input.enable()


            target_function = lambda: self.user_input.process_command()
            self.command_input_thread = threading.Thread(target=target_function)
            self.command_input_thread.start()
            
            if gui:
                self.neo_gui = NeoGlassesGUI(self.frame_queue)
                self.neo_gui_thread = threading.Thread(target=self.neo_gui.mainloop)
                self.neo_gui_thread.start()


            self.central_control.main_loop()

        
        except KeyboardInterrupt:
            # Graceful shutdown if the program is interrupted (e.g., Ctrl+C)
            if debug: print("Shutting down the system...")
        except Exception as e:
            if debug: print(f"An unexpected error occurred: {e}")
        finally:
            # Any final cleanup code can be placed here
            # This is important for releasing resources like file handles or network connections
            if self.user_input:
                self.user_input.disable()
            
            if self.central_control:
                self.central_control.deactivate()
            
            #TODO:
            # if self.neo_gui_thread.:
            #     self.neo_gui_thread.


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
