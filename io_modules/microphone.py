class MicrophoneModule:
    def __init__(self, microphone_index=0):
        self.microphone_index = microphone_index
        self.isEnabled = False

    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False