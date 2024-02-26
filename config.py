DEBUG_MODE = False
GUI_MODE = False

def set_debug_mode(status: bool):
    global DEBUG_MODE
    DEBUG_MODE = status
    
def set_gui_mode(status: bool):
    global GUI_MODE
    GUI_MODE = status

def is_debug_mode():
    return DEBUG_MODE

def is_gui_mode():
    return GUI_MODE