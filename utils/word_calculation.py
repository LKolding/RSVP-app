# from main.py
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
