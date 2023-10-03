#!/usr/bin/python3
# add 2 tuples  only for the first and second position
# and return a tuple of integers
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
