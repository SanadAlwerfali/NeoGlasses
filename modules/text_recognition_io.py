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
        _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
        se = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
        dilated = cv2.dilate(binary, se)
        text = pytesseract.image_to_string(dilated)

        is_text_detected = bool(text.strip())
        return is_text_detected, text, dilated

    def recognize_text(self, frame):
        is_detected, detected_text, dilated_frame = self.text_detection(frame)
        if self.isEnabled:
            if is_detected:
                self.frame_count += 1

            if self.frame_count >= self.frames_to_wait:
                text = detected_text

                self.frame_count = 0

                return text, dilated_frame

        return None, dilated_frame

    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False

    def __name__(self) -> str:
        return "TextRecognition"