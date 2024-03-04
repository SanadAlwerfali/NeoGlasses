class Mode:
    def __init__(self, camera=None, speaker=None, frame_queue=None):
        self.isActive = False
        self.camera = camera
        self.speaker = speaker
        self.frame_queue = frame_queue
    
    def activate(self, **kwargs):
        self.isActive = True
        self.settings = kwargs

    def deactivate(self):
        self.isActive = False
        self.settings = None

    def is_active(self):
        return self.isActive
        
    def main_loop(self):
        raise NotImplementedError("Subclasses should implement this!")
    
    def __name__(self) -> str:
        raise NotImplementedError("Subclasses should implement this!")
