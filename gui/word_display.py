import tkinter as tk
from tkinter import ttk

from utils.json_functions import get_settings
from utils.word_calculation import format_word


class WordText(tk.Text):
    
    def __init__(self, master: tk.Misc):

        super().__init__(
            master=master,
            height=1,
            width=30,
            borderwidth=0,
            highlightthickness=0,
            font=get_settings()['font']
            )
        root = self.winfo_toplevel()  # reference to Tk() instance -> background_color
        self.configure(background=root.background_color)
        
        
    def update_word(self, word:str):
        
        self.config(state="normal")
        self.delete("1.0", tk.END)
        self.insert("1.0", word)
        self._red_letter_indicator(word)
        self.config(state="disabled")
        
        
    def _red_letter_indicator(self, word:str):
        
        self.tag_delete('red')
        self.tag_config("red", foreground="red")
        
        # Compute which character should be red
        red_index = len(word)-20 # offset from the _right_

        start = f"1.{red_index}"
        end   = f"1.{red_index + 1}"

        self.tag_add("red", start, end)
        
    
class WordDisplay(tk.Frame):
    """
    Text display meant to display one word at a time.\n 
    This consists of a ttk.Label and a tk.Separator.\n
    This Frame should be displayed achored/sticky to the _right_. This is crucial.\n
    """
    def __init__(self, master: tk.Misc):
        
        tk.Frame.__init__(self, master)
        self._current_word = tk.StringVar(self, 'n/a')
        
        root = self.winfo_toplevel()
        self.configure(bg=root.background_color)

        #self._word_label = ttk.Label(master=self, textvariable=self._current_word, font= ('Menlo', get_settings()['textsize'], ""))
        self._word_label = WordText(self)
        self._word_label.insert(1.0, "n/a")
        
        self._separator = ttk.Separator(self)
        self._grid_widgets()
        
        
    def set_word(self, word:str) -> None:
        
        word = format_word(word, 20)
        self._word_label.update_word(word)
    
    
    def _grid_widgets(self):
        
        self._separator.pack(fill='x', side=tk.BOTTOM)
        self._word_label.pack(fill='x', side=tk.BOTTOM)
