#!/usr/bin/python3
"""
    prints a text with 2 new lines after each of these characters: ., ? and :
    otherrwise raise typeerror exception
"""


def text_indentation(text):
    """ validation """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """ create a list of my separators and copy text in new text """
    sep_list = ['.', '?', ':']
    idx_prev = 0

    """ print the text """
    for i in range(len(text)):
        if i == len(text) - 1:
            print(text[idx_prev:i + 1], end="")
        elif text[i] in sep_list:
            print(text[idx_prev:i + 1] + '\n')
            idx_prev = i + 1
            while text[idx_prev] == " ":
                idx_prev += 1
