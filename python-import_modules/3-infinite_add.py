#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg = argv[1:]
    sum = 0
    for i in (arg):
        sum += int(i)
    print(sum)
