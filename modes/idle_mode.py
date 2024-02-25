from modes.mode import Mode

class IdleMode(Mode):
    def __init__(self, control_module, frame_queue):
        super().__init__()
        self.frame_queue = frame_queue
        self.control_module = control_module
        
    def activate(self):
        self.isActive = True

    def deactivate(self):
        self.isActive = False

    def main_loop(self):
            #while self.isActive:
            #write the logic here
            pass

    def __name__(self) -> str:
        return "Idle"
