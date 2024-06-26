#!/usr/bin/python3
""" Square Class with an init """


class Square:
    """Square Class

    A Square Class

    """
    def __init__(self, size=0):
        """__init__

        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`.

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the current square area

        """
        return self.__size ** 2
