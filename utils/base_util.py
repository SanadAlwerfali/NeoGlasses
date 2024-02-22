class Util:

    isEnabled = False

    def enable(self):
        raise NotImplementedError("Subclasses should implement this!")

    def disable(self):
        raise NotImplementedError("Subclasses should implement this!")
    
    def __name__(self) -> str:
        raise NotImplementedError("Subclasses should implement this!")