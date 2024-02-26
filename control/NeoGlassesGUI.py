from queue import Queue
import tkinter as tk
import threading
import cv2
from PIL import Image, ImageTk

from control.control import CentralControlModule
from modes.text_reading_mode import TextReadingMode
from io_modules.camera import CameraModule

class NeoGlassesGUI(tk.Tk):
    def __init__(self, frame_queue):
        super().__init__()
        
        self.frame_queue = frame_queue
        self.title("NeoGlasses App")
        
        self.geometry("900x400")


        self.left_frame = tk.Frame(self)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.right_frame = tk.Frame(self)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.img = None

        self.display_frame()

        self.display_activation_status()

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.after(10, self.update_gui)

    def display_frame(self):
        if not self.frame_queue.empty():
            frame = self.frame_queue.get()
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = ImageTk.PhotoImage(Image.fromarray(frame_rgb))
            for widget in self.left_frame.winfo_children():
                widget.destroy()

            self.img_label = tk.Label(self.left_frame, image=img)
            self.img_label.image = img
            self.img_label.pack()

        self.after(10, self.display_frame)

    def display_activation_status(self):
        #TODO here we can add system status (or i/o status)
        self.after(1000, self.display_activation_status)

    def update_gui(self):
        self.display_frame()
        self.display_activation_status()
        self.after(10, self.update_gui)