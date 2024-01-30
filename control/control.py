# Central Control Module

from io_utils.camera import CameraModule
from modules.object_detection import ObjectDetectionModule


class CentralControlModule:
    def __init__(self):
        # Initialize modules
        self.camera_module = CameraModule(self)
        self.object_detection_module = ObjectDetectionModule(self)
        # ... other module initializations

        self.current_mode = None

    def switch_mode(self, new_mode):
        # Deactivate modules from the current mode
        self.deactivate_modules(self.current_mode)

        # Activate modules for the new mode
        self.activate_modules(new_mode)

        self.current_mode = new_mode

    def activate_modules(self, mode):
        if mode == 'ObjectDetection':
            self.camera_module.activate()
            self.object_detection_module.activate()
            # ... other module activations for this mode
        elif mode == 'TextReading':
            # ... activations for text reading mode
            pass
        # ... other mode activations

    def deactivate_modules(self, mode):
        if mode == 'ObjectDetection':
            self.camera_module.deactivate()
            self.object_detection_module.deactivate()
            # ... other module deactivations for this mode
        elif mode == 'TextReading':
            # ... deactivations for text reading mode
            pass
        # ... other mode deactivations

    def receive_notification(self, module_name, data):
        # Handle notifications and possibly switch modes
        if data == 'SwitchToTextReading':
            self.switch_mode('TextReading')
        # ... other notification handling

    def main_loop(self):
        # Main loop logic
        pass
