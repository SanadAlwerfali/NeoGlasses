import cv2

from modes.mode import Mode
from io_modules.camera import CameraModule
from modules.text_recognition_io import TextRecognitionModule

class TextReadingMode(Mode):
    def __init__(self, frame_queue):
        super().__init__()
        self.frame = None
        self.camera = CameraModule()
        self.text_recognition = TextRecognitionModule()
        self.frame_queue = frame_queue

    def activate(self):
        self.isActive = True
        # Enable necessary modules for text reading
        self.camera.enable()
        self.text_recognition.enable()

    def deactivate(self):
        self.isActive = False
        # Disable the modules when leaving text reading mode
        self.camera.disable()
        self.text_recognition.disable()

    def main_loop(self):
        while True:
            self.frame = self.camera.get_next_frame()
            recognized_text, dilated_frame = self.text_recognition.recognize_text(self.frame)
            
            display_frame = cv2.resize(dilated_frame, (600, 400))
            self.frame_queue.put(display_frame)
            
            if recognized_text:
                print("Recognized Text:", recognized_text)
                break
                # give a call to the speaker module to handle the text-to-speech
            
        self.camera.disable()
        self.deactivate()

    def __name__(self):
        return "TextReading"