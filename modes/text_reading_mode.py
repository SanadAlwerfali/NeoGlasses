import cv2
from modes.mode import Mode

class TextReadingMode(Mode):
    def __init__(self, control_module):
        super().__init__()
        self.control_module = control_module
        self.frame = None
        self.camera = control_module.io_modules['camera']
        self.text_recognition = control_module.modules['text_recognition']

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


            if recognized_text:
                self.frame = dilated_frame
                print("Recognized Text:", recognized_text)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.camera.disable()
        self.deactivate()

    def __name__(self):
        return "TextReading"