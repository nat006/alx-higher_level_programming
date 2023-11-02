#!/usr/bin/python3
import calculator_1

a = 10
b = 5

addition = calculator_1.add(a, b)
subtraction = calculator_1.subtract(a, b)
multiplication = calculator_1.multiply(a, b)
division = calculator_1.divide(a, b)

print("{} + {} = {}".format(a, b, addition))
print("{} - {} = {}".format(a, b, subtraction))
print("{} * {} = {}".format(a, b, multiplication))
print("{} / {} = {}".format(a, b, division))
