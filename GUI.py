import tkinter as tk
from tkinter import ttk

import sys  # for sys.argv

from text_engine import TextEngine

from utils.word_calculation import get_offset_from_word
from utils.json_functions import get_settings

# --- Tkinter ---

# Text display meant to display one word at a time
class WordDisplay(tk.Frame):
    def __init__(self, master: tk.Misc):
        tk.Frame.__init__(self, master)
        self._current_word = tk.StringVar(self, 'n/a')
        self._word_label = ttk.Label(master=self, textvariable=self._current_word, font= ('Courier New', get_settings()['textsize'], ""))
        self._separator = ttk.Separator(self)
        self._grid_widgets()
        
    def set_word(self, word:str) -> None:
        self._current_word.set(f'{word:>25}')
    
    def _grid_widgets(self):
        self._separator.pack(fill='x', side=tk.BOTTOM)
        self._word_label.pack(fill='x', side=tk.BOTTOM)


# Main Application Window
class ApplicationWindow(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        self._init()
        
    def _init(self):
        self.should_reset: bool = False
        self.isPaused: bool = False
        self._progressIntVar = tk.IntVar(self, 0)
        
        # --- Widgets ---
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # 1st row
        self._wordDisplay = WordDisplay(self)
        
        # 2nd row
        self.begin_btn = ttk.Button(self, text="Reset", command=self._reset)    
        self.pause_btn = ttk.Button(self, text="Pause/unpause", command=self._togglePause)

        # 3rd row
        self._progressBar = ttk.Progressbar(self,variable=self._progressIntVar)

        self._grid_widgets()
    
    def update(self) -> None:
        self._grid_widgets()
        return super().update()
        
    def _grid_widgets(self) -> None:
        self._wordDisplay.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=12, pady=20)
        self.begin_btn.grid(row=2, column=0, sticky=tk.SW)
        self.pause_btn.grid(row=2, column=1, sticky=tk.SE)
        self._progressBar.grid(row=3, column=0, columnspan=2, sticky=tk.S)
        
    def _reset(self):
        self._init()
        self.update()
        self.should_reset = not self.should_reset

    def _togglePause(self):
        self.isPaused = not self.isPaused
        
        
# Application
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("RSVP App")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._app_window = ApplicationWindow()
        self._grid_widgets()
        
    def update(self) -> None:
        self._grid_widgets()
        return super().update()
    
    def _grid_widgets(self) -> None:
        self._app_window.grid(sticky=tk.NSEW, padx=10, pady=10)
        


if __name__=="__main__":
    TEXT = " "
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            TEXT = f.read()
    else:
        TEXT = 'the quick brown fox jumps over the lazy dog'
        
    app = Application()
    engine = TextEngine(TEXT)
    
    timeout: float = 1.0  # milliseconds
    
    def update_word_and_get_timeout() -> float:
        word, timeout = engine.next()
        app._app_window._wordDisplay.set_word(word + ' '*get_offset_from_word(word, 20))
        return timeout
    
    def update_progress_bar() -> None:
        app._app_window._progressIntVar.set(round(engine._iterator / len(engine._words)*100 ))
    
    def logic() -> None:
        global timeout
        
        update_progress_bar()
        
        # Reset
        if app._app_window.should_reset:
            engine.reset()
            app._app_window.should_reset = not app._app_window.should_reset
            
            if app._app_window.isPaused:
                timeout = update_word_and_get_timeout()
        
        # Pause/unpause
        if not app._app_window.isPaused:
            timeout = update_word_and_get_timeout()
            
        app._app_window._wordDisplay.after( int(timeout*1000), logic)
        
        
    logic()
    app.mainloop()
        