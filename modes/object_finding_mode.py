from modes.mode import Mode

class ObjectFindingMode(Mode):

    def __init__(self, control_module, frame_queue):
        super().__init__()

        self.control_module = control_module
        self.frame_queue = frame_queue

    def activate(self):
        self.isActive = True

        # Enable necessary modules for object finding
        self.control_module.io_modules['camera'].enable()
        self.control_module.modules['object_detection'].enable()

    def deactivate(self):
        self.isActive = False

        # Disable the modules when leaving object finding mode
        self.control_module.io_modules['camera'].disable()
        self.control_module.modules['object_detection'].disable()

    def main_loop(self):
        while self.isActive:
            #write the logic here
            pass


    def __name__(self):
        return "ObjectFinding"