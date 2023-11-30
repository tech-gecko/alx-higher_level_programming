#!/usr/bin/python3
def uppercase(str):
    for index, char in enumerate(str):
        if (ord(char) >= 97) and (ord(char) <= 122):
            char = chr(ord(char) - 32)
        print("{}".format(char), end='')

        if index == len(str) - 1:
            print("\n")
