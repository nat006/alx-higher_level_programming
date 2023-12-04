#!/usr/bin/python3
class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)
