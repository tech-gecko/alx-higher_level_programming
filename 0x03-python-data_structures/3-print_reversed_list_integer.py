#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_reversed_list = my_list[::-1]

    for integer in my_reversed_list:
        print("{}".format(integer))
