from tkinter import *
from tkinter import ttk


from main import get_offset_from_word


def iterate_text(text: str):
    for word in text.split():
        yield word


class app_data:
    text = "Now news came to Hithlum that Dorthonion was lost and the sons of Finarfin overthrown, and that the sons of Fëanor were driven from their lands. Then Fingolfin beheld the utter ruin of the Noldor, and the defeat beyond redress of all their houses; and filled with wrath and despair he mounted upon Rochallor his great horse and rode forth alone, and none might restrain him. He passed over Dor-nu-Fauglith like a wind amid the dust, and all that beheld his onset fled in amaze, thinking that Oromë himself was come: for a great madness of rage was upon him, so that his eyes shone like the eyes of the Valar. Thus he came alone to Angband's gates, and he sounded his horn, and smote once more upon the brazen doors, and challenged Morgoth to come forth to single combat. And Morgoth came. "


class gui_data:
    root = Tk()
    root.title("RSVP | Reading tool")

    frm = ttk.Frame(root, padding=10)
    frm.grid(sticky=NSEW, padx = 10, pady= 10)

    current_word: StringVar = StringVar(frm, "consequential")

    # 1st row (logo/title)
    logo_label = ttk.Label(frm, text="RSVP | Reading tool", justify=CENTER).grid(column=0, row=0, columnspan=2, padx = 10, pady = 10)

    # 2nd row
    word_label = ttk.Label(master=frm, textvariable=current_word, border="6", justify=RIGHT, padding=20).grid(column=0, row=1, columnspan=2, sticky=E)

    # 3rd row
    begin_btn = ttk.Button(frm, text="Begin").grid(column=0, row=2)
    pause_btn = ttk.Button(frm, text="Pause").grid(column=1, row=2)

    # 4th row
    quit_btn  = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3, columnspan=2, sticky=E)

    def update_word(word: str) -> bool:
        pass



class AppGUI:
    def __init__(self):
        pass

    def run(self): 
        gui_data.root.mainloop()
