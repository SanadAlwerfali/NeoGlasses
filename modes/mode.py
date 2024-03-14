class Mode:
    def __init__(self):
        self.isActive = None
    
    def activate(self):
        raise NotImplementedError("Subclasses should implement this!")

    def deactivate(self):
        raise NotImplementedError("Subclasses should implement this!")
        
    def main_loop(self):
        raise NotImplementedError("Subclasses should implement this!")
    
    def get_name(self):
        raise NotImplementedError("Subclasses should implement this!")
