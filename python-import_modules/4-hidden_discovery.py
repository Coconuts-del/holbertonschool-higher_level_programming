#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for nom in dir(hidden_4):
        if "__" != nom[:2]:
            print(nom)
