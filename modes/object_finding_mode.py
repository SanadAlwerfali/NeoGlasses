from modes.mode import Mode
from config import is_debug_mode

class ObjectFindingMode(Mode):

    def __init__(self, camera=None, speaker=None, frame_queue=None, yolo=None, text_to_speech=None):
        super().__init__(camera=camera, speaker=speaker, frame_queue=frame_queue, text_to_speech=text_to_speech)
        self.yolo = yolo

    def main_loop(self):
        #write the logic here
        if self.isActive and self.yolo is not None:
            target_label = self.settings.get('target_label', None)

            if is_debug_mode(): print(f"Looking for the object: {target_label}...")

            if target_label: # if target_label is not None
                self.text_to_speech.convert(f"Looking for {target_label}.")
                self.text_to_speech.convert("Please move the camera around.")
                while self.isActive:
                    # Look for the object
                    frame = self.camera.get_next_frame()
                    
                    try:
                        detected_objects = self.yolo.detect_objects(frame)
                    except Exception as e:
                        print(f"An error occurred while detecting objects: {e}")
                        self.deactivate()
                        break

                    for obj_name, confidence, bbox in detected_objects:
                        if obj_name == target_label:
                            # Once the object is found
                            if is_debug_mode(): print(f"{target_label} Found! With confidence {confidence}!")
                            # Announce the detection
                            self.text_to_speech.convert(f"{target_label} is infront of you.")
                            # Deactivate once object is found
                            self.deactivate()

            else:
                if is_debug_mode(): print("Object is not recognized.")
                self.text_to_speech.convert(f"Object is not recognized.")
                self.deactivate()


    def activate(self, **kwargs):
        self.settings = kwargs
        self.isActive = True
        self.camera.enable()

    def deactivate(self):
        self.settings = None
        self.isActive = False
        self.camera.disable()

    def __name__(self):
        return "ObjectFinding"