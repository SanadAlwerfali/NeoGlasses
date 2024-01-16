import cv2

class CameraFeedProvider:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)

        # Check if the camera opened successfully
        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            raise ValueError("Could not open camera.")
        
        cv2.namedWindow('Camera Feed', cv2.WINDOW_NORMAL)

    def get_next_frame(self):
        # Read a frame from the camera
        ret, frame = self.cap.read()

        if not ret:
            print("Error: Could not read frame.")
            return None

        return frame
    
    # Close the camera when done
    def release_camera(self):
        self.cap.release()