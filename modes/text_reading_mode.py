import cv2
from time import sleep
from modes.mode import Mode
from io_modules.camera import CameraModule
from modules.text_recognition_io import TextRecognitionModule
from modules.text_to_speech_io import TextToSpeechModule


class TextReadingMode(Mode):
    def __init__(self, camera=None, speaker=None, frame_queue=None):
        super().__init__(camera=camera, speaker=speaker, frame_queue=frame_queue)
        self.frame = None
        self.text_recognition = TextRecognitionModule()
        self.text__to_speech = TextToSpeechModule()

    def activate(self):
        self.isActive = True
        # Enable necessary modules for text reading
        self.camera.enable()
        self.text_recognition.enable()
        self.text__to_speech.enable()

    def deactivate(self):
        self.isActive = False
        # Disable the modules when leaving text reading mode
        self.camera.disable()
        self.text_recognition.disable()
        self.text__to_speech.disable()

    def main_loop(self):
        while self.isActive:
            self.frame = self.camera.get_next_frame()
            recognized_text, dilated_frame = self.text_recognition.recognize_text(self.frame)
            
            display_frame = cv2.resize(dilated_frame, (600, 400))
            self.frame_queue.put(display_frame)
            
            if recognized_text:
                print(recognized_text)
                self.text__to_speech.convert(recognized_text)
                break
                
        self.camera.disable()
        self.deactivate()

    def __name__(self):
        return "TextReading"