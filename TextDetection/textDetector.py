import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

class TextDetector:
    def __init__(self):
        self.frames_to_wait = 8  # Number of frames to wait after capturing the frame
        self.frame_count = 0
        
    # Helper method to check if there is a detectable text from the frame
    def is_text_detected(self, image):
        # Convert frame to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Reduce noise and improve text detection
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Extract text
        text = pytesseract.image_to_string(blurred)

        # return ture if text is detected
        return bool(text.strip())

    # Same logic as is_text_detected method except it returns the text
    def text_detection(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        text = pytesseract.image_to_string(blurred)

        return text

    def process_frame(self, frame):
        # Check for text detection
        if self.is_text_detected(frame):
            self.frame_count += 1

            # Wait few frames before capturing the frame
            if self.frame_count >= self.frames_to_wait:
                detected_text = self.text_detection(frame)

                self.frame_count = 0

                return detected_text

        return None
