DEBUG_MODE = False

def set_debug_mode(status: bool):
    global DEBUG_MODE
    DEBUG_MODE = status

def is_debug_mode():
    return DEBUG_MODE
