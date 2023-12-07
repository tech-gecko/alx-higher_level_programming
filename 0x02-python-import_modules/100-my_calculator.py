#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    # Set of allowed operators.
    allowed_operators = {'+', '-', '*', '/'}

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in allowed_operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        # Do the actual calculation.
        if sys.argv[2] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        if sys.argv[2] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        if sys.argv[2] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        if sys.argv[2] == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
