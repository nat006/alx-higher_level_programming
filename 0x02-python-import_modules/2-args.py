#!/usr/bin/python3
import sys

args = sys.argv[1:]
num_args = len(args)

print("Number of argument{}: {}".format("" if num_args == 1 else "s", num_args), end="")
if num_args > 0:
    print(":", end="")
else:
    print(".")

for i in range(num_args):
    print("{}: {}".format(i+1, args[i]))
