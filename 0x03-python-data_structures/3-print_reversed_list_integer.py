#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_reversed_list = my_list.reverse()

    for integer in my_reversed_list:
        print("{:d}".format(integer))