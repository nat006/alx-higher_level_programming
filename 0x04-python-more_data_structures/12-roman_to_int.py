#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_values = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
                    'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                    'V': 5, 'IV': 4, 'I': 1}
    num = 0
    i = 0
    strlen = len(roman_string)
    while i < strlen:
        if i < strlen - 1 and roman_string[i:i+2] in roman_values:
            num += roman_values[roman_string[i:i+2]]
            i += 2
        else:
            num += roman_values[roman_string[i]]
            i += 1
    return num
