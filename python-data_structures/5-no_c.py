#!/usr/bin/python3

def no_c(my_string):
    """ removes c an C from strings """
    new_str = [i for i in my_string if i != "c" and i != "C"]
    return ("".join(new_str))
