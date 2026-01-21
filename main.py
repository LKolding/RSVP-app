import time
import os
import sys
import json

import GUI

text2 = "Now news came to Hithlum that Dorthonion was lost and the sons of Finarfin overthrown, and that the sons of Fëanor were driven from their lands. Then Fingolfin beheld the utter ruin of the Noldor, and the defeat beyond redress of all their houses; and filled with wrath and despair he mounted upon Rochallor his great horse and rode forth alone, and none might restrain him. He passed over Dor-nu-Fauglith like a wind amid the dust, and all that beheld his onset fled in amaze, thinking that Oromë himself was come: for a great madness of rage was upon him, so that his eyes shone like the eyes of the Valar. Thus he came alone to Angband's gates, and he sounded his horn, and smote once more upon the brazen doors, and challenged Morgoth to come forth to single combat. And Morgoth came. "


def get_settings() -> dict:
    with open('settings.json', 'r') as f:
        return json.load(f)


def get_offset_from_word(w: str, right_spacing: int) -> int:
    '''
    Returns amount of whitespace to use for left hand side offset when printing with fstring (eg. {>:20} )
    
    :param w: Word to process
    :type w: str
    :return: Amount of whitespace
    :rtype: int
    '''
    # total offset
    offset: int = right_spacing

    if len(w) in (1, 2):
        offset -= 1
    
    elif len(w) == 3:
        offset -= 2

    elif len(w) == 4:
        offset -= 3

    elif len(w) in (5, 6):
        offset -= 4

    elif len(w) == 7:
        offset -= 5

    elif len(w) in (8, 9):
        offset -= 6

    elif len(w) == 10:
        offset -= 7

    elif len(w) == 11:
        offset -= 8

    elif len(w) == 12:
        offset -= 9

    elif len(w) in (12, 13):
        offset -= 10

    # temp
    elif len(w) > 13:
        offset -= 11

    return offset


def application_run(text: str):
    os.system('cls')

    SETTINGS = get_settings()

    LH_SPACING = 5
    RH_SPACING = 20

    for word in text.split():
        word_formatted = word + ' ' * get_offset_from_word(word, RH_SPACING)
        print(f'{word_formatted:>25}')

        letter_indicator = ' ' * LH_SPACING + '*' + ' ' * RH_SPACING
        print(letter_indicator)

        if word[-1] == '.':
            time.sleep(SETTINGS['timeouts']['full_stop'])

        if word[-1] == ';':
            time.sleep(SETTINGS['timeouts']['semicolon'])

        elif word[-1] == ',':
            time.sleep(SETTINGS['timeouts']['comma'])

        else:
            time.sleep(SETTINGS['timeouts']['default'])

        os.system('cls')


if __name__=="__main__":
    text: str = text2
    foo = len(sys.argv)
    if len(sys.argv) == 1:
        print('Please provide a text string (in "quotation" marks) as argument')
        exit()

    elif (len(sys.argv) == 2):
        pass
        #text = sys.argv[1]

    else:
        print('Incorrect argument(s) (correct usage: main.py "text in quotation marks")')
        exit()

    gui = GUI.AppGUI()
    gui.run()

    #application_run(text)