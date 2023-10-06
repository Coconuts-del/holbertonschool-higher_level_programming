#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print_elem = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            nb_print_elem += 1
    except IndexError:
        pass
    print()
    return nb_print_elem
