class SpeakerModule:
    def __init__(self, control_module, speaker_index=0):
        self.control_module = control_module
        self.speaker_index = speaker_index
        self.isEnabled = False