#!/usr/bin/python3
"""
   writes a string to a text file (UTF8)
   and returns the number of characters written
   create file if doesn't exist
   overwrite if exist
"""


def write_file(filename="", text=""):
    """write a file"""
    with open(filename, "w", encoding="utf-8") as file:
        nb = file.write(text)
    return nb
