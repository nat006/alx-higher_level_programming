#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1  # subtract 1 to exclude the name of the script
args_list = argv[1:]  # exclude the name of the script from the list

# Print number of arguments and the list of arguments
if num_args == 0:
    print("Number of argument(s): 0.")
else:
    if num_args == 1:
        print("Number of argument(s): 1. Argument:")
    else:
        print(f"Number of argument(s): {num_args}. Arguments:")

    for i, arg in enumerate(args_list):
        print(f"{i+1}: {arg}")

    print()
