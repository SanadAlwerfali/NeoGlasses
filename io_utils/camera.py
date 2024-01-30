import cv2

class CameraModule:
    def __init__(self, control_module, camera_index=0):
        self.control_module = control_module
        self.camera_index = camera_index
        self.capture = cv2.VideoCapture(self.camera_index)

        if not self.capture.isOpened():
            print("Error: Could not open camera.")
            raise ValueError("Could not open camera.")
        
        cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)

    def get_next_frame(self):
        ret, frame = self.capture.read()

        if not ret:
            print("Error: Could not read frame.")
            return None

        return frame
    
    def release_camera(self):
        self.capture.release()