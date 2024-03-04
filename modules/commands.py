class Commands:
    COMMANDS_LIST = {
        "find": "ObjectFinding",
        "read": "TextReading",
        "idle": "Idle"
    }

    YOLO = None

    def __init__(self, yolo):
        Commands.YOLO = yolo

    @staticmethod
    def get_command_mode(command_text):
        # Loop through each command to see if it's in the command_text
        for command, mode in Commands.COMMANDS_LIST.items():
            if command in command_text:
                return mode
        return "Idle"  # Return a default mode if no command is matched

    @staticmethod
    def get_object_label(command_text):
        # Checks YOLO's available classes
        for obj in Commands.YOLO.available_classes:
            if obj in command_text:
                return obj
        return None