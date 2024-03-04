class SpeakerModule:
    def __init__(self, speaker_index=0):
        self.speaker_index = speaker_index
        self.isEnabled = False

    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False