#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    nb_arg = len(argv[1:])
    if nb_arg == 0:
        print("0 arguments.")
    elif nb_arg > 1:
        print("{} arguments:".format(nb_arg))
    else:
        print("1 argument:")
    for i in range(1, nb_arg + 1):
        print("{}: {}".format(i, argv[i]))
