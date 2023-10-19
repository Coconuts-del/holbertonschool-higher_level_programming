#!/usr/bin/python3
"""
   append a string to a text file (UTF8)
   and returns the number of characters added
   create file if doesn't exist
"""


def append_write(filename="", text=""):
    """append in a file"""
    with open(filename, "a", encoding="utf-8") as file:
        nb = file.write(text)
    return nb
