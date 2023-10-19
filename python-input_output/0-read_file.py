#!/usr/bin/python3
""" read a file(UTF8) and prints it to stdout """


def read_file(filename=""):
    """ read  and print a file """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")
