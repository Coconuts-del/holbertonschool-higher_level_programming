#!/usr/bin/python3
"""
    prints a text with 2 new lines after each of these characters: ., ? and :
    otherrwise raise typeerror exception
"""


def text_indentation(text):
    """ validationn """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """ create a list of my separators and copy text in new text """
    sep_list = ['. ', '? ', ': ']
    new_text = text

    """ modify the sep in new_text and print """
    for sep in sep_list:
        new_text = new_text.replace(sep, sep[0:1] + '\n\n')
    print(new_text)
