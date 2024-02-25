import subprocess
import pyttsx3

class SpeakerModule:
    def __init__(self, control_module):
        self.control_module = control_module
        self.isEnabled = False
        self.process = None 
        self.enabled = False
        self.rate = 150  # Arbitrary constant value of 150 based on testing

    def enable(self):
        self.enabled = True

    def speak(self, text):
        if not self.enabled:
            print("Speaker is not enabled. Call 'enable()' to start speaking.")
            return
        
        # Kill previous subprocess before speaking
        self._terminate_process()

        # Create a sub process to allow for termination while speaking
        self.process = subprocess.Popen( 
            ["python3", "-c", self._get_speak_command(text)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

    def _terminate_process(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()

    # Helper function to get the commands for the sub process
    def _get_speak_command(self, text):
        return (
            f"from pyttsx3 import init;"
            f"engine = init();"
            f"engine.setProperty('rate', {self.rate});"
            f"engine.say('{text}');"
            f"engine.runAndWait();"
        )

    def interrupt(self):
        self._terminate_process()
    
    def disable(self):
        self.interrupt()
