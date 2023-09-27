#!/usr/bin/python3
# prints all numbers from 00 to 99 with "," as separator
for number in range(0, 100):
    if number < 99:
        print("{:02}, ".format(number), end="")
    else:
        print("{}".format(number))
