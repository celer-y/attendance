import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sys

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance")
        self.root.geometry("1366x768")

        # Add your GUI elements here

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            sys.exit()
