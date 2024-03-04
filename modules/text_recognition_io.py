# Text Recognition and Processing Module
import cv2
import numpy as np
import pytesseract

class TextRecognitionModule:
    def __init__(self):
        super().__init__()
        self.frames_to_wait = 8  
        self.frame_count = 0
        self.isEnabled = True

    def text_detection(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
        se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        dilated = cv2.dilate(binary, se)
        try:
            text = pytesseract.image_to_string(dilated)
        except:
            raise ValueError("pytesseract could not detect text.")
        
        is_text_detected = bool(text.strip())
        return is_text_detected, text, dilated

    def recognize_text(self, frame):
        #FIXME: Logic Needs fixing, it is not waiting for frames to be processed as the frame has already been captured

        if self.isEnabled:
            is_detected, text, dilated_frame= self.text_detection(frame)
            
            if is_detected:
                self.frame_count += 1

            if self.frame_count >= self.frames_to_wait:
                _, detected_text, dilated_frame = self.text_detection(frame)
                self.frame_count = 0

                return detected_text, dilated_frame

        return None, dilated_frame

    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False

    def __name__(self) -> str:
        return "TextRecognition"