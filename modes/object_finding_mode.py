import cv2
from modes.mode import Mode
from io_modules.camera import CameraModule
from modules.object_detection_io import ObjectDetectionModule
class ObjectFindingMode(Mode):

    def __init__(self, frame_queue):
        super().__init__()
        self.frame = None
        self.camera = CameraModule()
        self.object_detection = ObjectDetectionModule()
        self.frame_queue = frame_queue

    def activate(self):
        self.isActive = True

        # Enable necessary modules for object finding
        self.camera.enable()
        self.object_detection.enable()

    def deactivate(self):
        self.isActive = False

        # Disable the modules when leaving object finding mode
        self.camera.disable()
        self.object_detection.disable()

    def main_loop(self):
        while self.isActive:
            #write the logic here
            self.frame = self.camera.get_next_frame()
            self.frame_queue.put(self.frame)
            pass


    def __name__(self):
        return "ObjectFinding"