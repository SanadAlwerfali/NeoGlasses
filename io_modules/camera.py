import cv2

from config import is_debug_mode

class CameraModule:
    def __init__(self, control_module, camera_index=1):
        
        pass

        self.control_module = control_module
        self.camera_index = camera_index

    def enable(self):
        self.cam = cv2.VideoCapture(self.camera_index)

        if not self.cam.isOpened():
            raise ValueError("Could not open camera.")

    def get_next_frame(self):
        ret, frame = self.cam.read()

        if not ret:
            if is_debug_mode(): print("Error: Could not read frame.")
            return None

        return frame
    
    def disable(self):
        self.cam.release()