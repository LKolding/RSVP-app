import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import platform

from collections.abc import Callable

from gui.word_display import WordDisplay


class ControlsUI(tk.Frame):

    def __init__(self, master: tk.Misc, reset_func: Callable, pause_func: Callable):
        super().__init__(master)
        # Reset button
        self._reset_btn = tk.Button(self, text="Reset", command=reset_func)
        # Pause/unpause button
        img = Image.open("assets\\play.png" if platform.system() == 'Windows' else "assets/play.png")
        img = img.resize((64, 64), Image.LANCZOS)
        self._play_img = ImageTk.PhotoImage(img)
        self._pause_btn = tk.Button(self, text="empty", command=pause_func, image=self._play_img)

        self._grid_widgets()


    def _grid_widgets(self):
        self._reset_btn.grid(row=0, column=0)
        self._pause_btn.grid(row=0, column=1)


# Main Application Window
class ApplicationWindow(tk.Frame):
    
    def __init__(self):
        
        tk.Frame.__init__(self)
        self._should_reset: bool = False
        self._isPaused: bool = True
        self._progressIntVar = tk.IntVar(self, 0)
        self._current_wpm = tk.StringVar(self, "WPM: 0")
        
        root = self.winfo_toplevel()
        self.configure(bg=root.background_color)

        # --- Widgets ---
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)
        
        # 1st row
        self._wordDisplay = WordDisplay(self)
        # 2nd row
        self._controls = ControlsUI(self, self._togglePause, self._reset)
        # 3rd row
        self._progressBar = ttk.Progressbar(self, variable=self._progressIntVar)
        self._wpm_indicator = ttk.Label(self, textvariable=self._current_wpm, font=("",24,""))
        
        self._grid_widgets()
        

    def _grid_widgets(self) -> None:
        
        self._wordDisplay.grid(row=0, column=0)
        self._controls.grid(row=1, column=0)
        self._progressBar.grid(row=2, column=0)
        self._wpm_indicator.grid(row=2, column=0, sticky=tk.E)
        
        
    def _reset(self) -> None:

        self._should_reset = True


    def _togglePause(self) -> None:

        self._isPaused = not self._isPaused
        

# Application
class Application(tk.Tk):
    
    DEFAULT_BACKGROUND_COLOR:str

    def __init__(self):
        
        tk.Tk.__init__(self)
        self.wm_title("RSVP App")
        self._store_bg_color()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self._app_window = ApplicationWindow()

        self._grid_widgets()
    

    def _store_bg_color(self):

        Application.DEFAULT_BACKGROUND_COLOR = self.cget('bg')
        self.background_color = self.cget('bg')


    def _grid_widgets(self) -> None:

        self._app_window.grid(row=0, column=0, sticky=tk.NSEW)
        
