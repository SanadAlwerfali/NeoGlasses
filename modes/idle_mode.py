from modes.mode import Mode

class IdleMode(Mode):
    def __init__(self, control_module):
        super().__init__()

        self.control_module = control_module
        
    def activate(self):
        pass

    def deactivate(self):
        pass

    def __name__(self) -> str:
        return "Idle"