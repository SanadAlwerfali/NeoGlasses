from modes.mode import Mode

class ObjectFindingMode(Mode):

    def __init__(self, control_module):
        super().__init__()
        
        self.control_module = control_module

    def activate(self):
        # Enable necessary modules for object finding
        self.control_module.io_modules['camera'].enable()
        self.control_module.modules['object_detection'].enable()

    def deactivate(self):
        # Disable the modules when leaving object finding mode
        self.control_module.io_modules['camera'].disable()
        self.control_module.modules['object_detection'].disable()

    def __name__(self):
        return "ObjectFinding"