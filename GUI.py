import tkinter as tk
from tkinter import ttk

from gui.word_display import WordDisplay

from utils.json_functions import get_settings

# Main Application Window
class ApplicationWindow(tk.Frame):
    
    def __init__(self):
        
        tk.Frame.__init__(self)
        self._init()
        
        
    def _init(self):
        
        self.should_reset: bool = False
        self.isPaused: bool = True
        self._progressIntVar = tk.IntVar(self, 0)
        
        # --- Widgets ---
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # 1st row
        self._wordDisplay = WordDisplay(self)
        # 2nd row
        self.reset_btn = ttk.Button(self, text="Reset", command=self._reset)
        self.dummy_btn = ttk.Button(self, text='fisse')  # temp
        # 4rd row
        self._progressBar = ttk.Progressbar(self,variable=self._progressIntVar, length=200)
        
        self._grid_widgets()
    

    def _grid_widgets(self) -> None:
        
        self._wordDisplay.grid(row=0, column=0, padx=12, pady=20)
        self.reset_btn.grid(row=2, column=0, padx=6, pady=6)
        self.dummy_btn.grid(row=4, column=0, padx=6, pady=6)  # temp
        self._progressBar.grid(row=3, column=0, sticky=tk.S, pady=8)
        
        
    def _reset(self):
        self.should_reset = True


    def _togglePause(self):
        self.isPaused = not self.isPaused
        

# Application
class Application(tk.Tk):
    
    def __init__(self):
        
        tk.Tk.__init__(self)
        self.wm_title("RSVP App")
        self.configure(background=get_settings()['background_color'])

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._app_window = ApplicationWindow()
        self._app_window.configure(background=get_settings()['background_color'])
        self._grid_widgets()
    
    
    def _grid_widgets(self) -> None:
        self._app_window.grid(sticky=tk.NSEW, padx=10, pady=10)
        
