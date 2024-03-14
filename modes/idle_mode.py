from modes.mode import Mode

class IdleMode(Mode):
    def __init__(self, camera=None, speaker=None, frame_queue=None):
        super().__init__(camera=camera, speaker=speaker, frame_queue=frame_queue)

    def main_loop(self):
            pass

    def __name__(self) -> str:
        return "Idle"
