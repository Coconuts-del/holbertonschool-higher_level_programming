#!/usr/bin/python3
for nb1 in range(0, 10):
    for nb2 in range(nb1 + 1, 10):
        if nb1 == 8:
            print("{}{}".format(nb1, nb2))
        else:
            print("{}{}".format(nb1, nb2), end=", ")
