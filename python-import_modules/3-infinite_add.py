#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    if argv:
        total = sum(int(arg) for arg in argv)
    else:
        total = 0
    print(f"{total}")
