#!/usr/bin/python3
# print all numbers from 00 to 99
for number in range(0, 100):
    if number == 99:
        print(number)
    else:
        print("{:02}".format(number), end=", ")
