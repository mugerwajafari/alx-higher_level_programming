#!/usr/bin/python3
"""print function added"""


class Square:
    """Square class

    """

    def __init__(self,size=0):
        """
        Raises:
        if size not int raise TypeError
        if size < ValueError
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.size = size
       
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')
         
        self.size = size
    
    def area(self):
        """Returns the current square area         """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return None

        for i in range(1, self.area() + 1):
            print('#', end='')

            if i % self.__size == 0 and i > 0:
                print()
