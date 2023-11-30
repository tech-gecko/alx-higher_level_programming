#!/usr/bin/python3
def remove_char_at(string_, n):
    if (n < 0 or n > len(string_)):
        return (string_)
    new_one = string_[:n]
    new_one += string_[n + 1:]
    return (new_one)
