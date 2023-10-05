#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return([replace if i == search else i for i in my_list])
    """ list_result = my_list[:]
    for i in range(len(my_list)):
        if list_result[i] is search:
            list_result[i] = replace
    return (list_result) """
