#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nums = set(my_list)
    result = 0
    for num in unique_nums:
        result += num
    return result
