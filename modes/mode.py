class Mode:
    def __init__(self):
        self.isActive = None
    
    def activate(self):
        raise NotImplementedError("Subclasses should implement this!")

    def deactivate(self):
        raise NotImplementedError("Subclasses should implement this!")

    def is_active(self) -> bool:
        return self.isActive
        
    def main_loop(self):
        raise NotImplementedError("Subclasses should implement this!")
    
    def __name__(self) -> str:
        raise NotImplementedError("Subclasses should implement this!")
