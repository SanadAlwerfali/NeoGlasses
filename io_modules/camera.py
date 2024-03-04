import cv2

from config import is_debug_mode

class CameraModule:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.isEnabled = False

    def enable(self):
        self.cam = cv2.VideoCapture(self.camera_index)
        if not self.cam.isOpened():
            raise ValueError("Could not open camera.")
        self.isEnabled = True

    def normalize_brightness(self, frame):
        normalized_frame = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX)
        return normalized_frame
    
    def get_next_frame(self):
        ret, frame = self.cam.read()

        if not ret:
            if is_debug_mode(): print("Error: Could not read frame.")
            return None

        return self.normalize_brightness(frame)
    
    def disable(self):
        self.cam.release()
        self.isEnabled = False