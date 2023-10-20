#!/usr/bin/python3
"""
    Write a script that adds all arguments to a Python list,
    and then save them to a file
"""
import sys

"""json functions"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""constants"""
filename = "add_item.json"
ARGS = sys.argv[1:]


def main():
    """ load file """
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    """ update list """
    my_list += ARGS

    """save in json file"""
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
