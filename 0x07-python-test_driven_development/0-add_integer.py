#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function adds two integers if two arguments are passed
    and if only one is passed, it adds it to 98.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    return (int(a) + int(b))


if __name__ == '__main__':
    import doctest
    doctest.testfile('0-add_integer.txt')
