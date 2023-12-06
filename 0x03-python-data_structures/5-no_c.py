#!/usr/bin/python3

def no_c(my_string):
    no_c_string = ''.join(char for char in my_string
                              if char.lower() not in {'c'})
    return (no_c_string)
