#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number % 10
if a > 5:
    b = "and is greater than 5"
elif a == 0:
    b = "and is 0"
elif a < 6 and a != 0:
    b = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, a, b))
