#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print(f"{argc} arguments.")
    elif argc == 1:
        print(f"{argc} argument:")
    else:
        print(f"{argc} arguments:")
    for i in range(1, argc + 1):
        print(f"{i}: {argv[i]}")
