class Mode:
    
    def activate(self):
        raise NotImplementedError("Subclasses should implement this!")

    def deactivate(self):
        raise NotImplementedError("Subclasses should implement this!")
    
    def __name__(self) -> str:
        raise NotImplementedError("Subclasses should implement this!")
