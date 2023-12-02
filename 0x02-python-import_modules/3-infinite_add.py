#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv)) == 1:
        print("0")
    else:
        print("{}".format(sum(int(i) for i in sys.argv[1:])))
