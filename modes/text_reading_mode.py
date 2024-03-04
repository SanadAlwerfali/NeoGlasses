import cv2
from modes.mode import Mode
from modules.text_recognition_io import TextRecognitionModule

class TextReadingMode(Mode):
    def __init__(self, camera=None, speaker=None, frame_queue=None):
        super().__init__(camera=camera, speaker=speaker, frame_queue=frame_queue)
        self.text_recognition = TextRecognitionModule()

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

    def is_active(self):
        return self.isActive

    def main_loop(self):
        while self.isActive:
            frame = self.camera.get_next_frame()
            recognized_text, dilated_frame = self.text_recognition.recognize_text(self.frame)
            
            display_frame = cv2.resize(dilated_frame, (600, 400))
            self.frame_queue.put(display_frame)
            
            if recognized_text:
                #TODO: give a call to the speaker module to handle the text-to-speech
                print("Recognized Text:", recognized_text)
                self.deactivate()

    def __name__(self):
        return "TextReading"