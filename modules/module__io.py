class ModuleIO:

    isEnabled = False

    def enable(self):
        raise NotImplementedError("Subclasses should implement this!")

    def disable(self):
        raise NotImplementedError("Subclasses should implement this!")

    def isEnabled(self):
        return self.isEnabled
    
    def __name__(self) -> str:
        raise NotImplementedError("Subclasses should implement this!")