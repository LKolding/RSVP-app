import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import platform

from gui.word_display import WordDisplay

from utils.json_functions import get_settings


# Main Application Window
class ApplicationWindow(tk.Frame):
    
    def __init__(self):
        
        tk.Frame.__init__(self)
        self._should_reset: bool = False
        self._isPaused: bool = True
        self._progressIntVar = tk.IntVar(self, 0)
        
        root = self.winfo_toplevel()
        self.configure(bg=root.background_color)

        # --- Widgets ---
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # 1st row
        self._wordDisplay = WordDisplay(self)
        # 2nd row
        self._reset_btn = tk.Button(self, text="Reset", command=self._reset)

        img = Image.open("assets\\play.png" if platform.system() == 'Windows' else "assets/play.png")
        img = img.resize((64, 64), Image.LANCZOS)
        self._play_img = ImageTk.PhotoImage(img)
        self._pause_btn = tk.Button(self, text='Pause/unpause', image=self._play_img)

        # 4rd row
        self._progressBar = ttk.Progressbar(self,variable=self._progressIntVar)
        
        self._grid_widgets()
        

    def _grid_widgets(self) -> None:
        
        self._wordDisplay.grid(row=0, column=0, padx=12, pady=20)
        self._reset_btn.grid(row=1, column=0)
        self._pause_btn.grid(row=2, column=0)
        self._progressBar.grid(row=3, column=0, sticky=tk.S, pady=8)
        
        
    def _reset(self) -> None:

        self._should_reset = True


    def _togglePause(self) -> None:

        self._isPaused = not self._isPaused
        

# Application
class Application(tk.Tk):
    
    def __init__(self):
        
        tk.Tk.__init__(self)
        self.wm_title("RSVP App")
        self._init()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self._app_window = ApplicationWindow()
        #self._app_window.configure(background=get_settings()['background_color'])
        self._grid_widgets()
    

    def _init(self):

        self.background_color = self.cget('bg')

    
    def _grid_widgets(self) -> None:

        self._app_window.grid(sticky=tk.NSEW, padx=10, pady=10)
        
