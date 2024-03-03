class Commands:
    COMMAND_LIST = {
        "find": "ObjectDetection",
        "read": "TextReading",
        "default": "Idle" #might want to add more keywords for each mode ex: sleep > Idle
    }

    @staticmethod
    def get_command_mode(command_text):
        if command_text is None:
            return "Idle"
        # Loop through each command to see if it's in the command_text
        for command, mode in Commands.COMMAND_LIST.items():
            if command in command_text:
                return mode
        return "Idle"  # Return a default mode if no command is matched