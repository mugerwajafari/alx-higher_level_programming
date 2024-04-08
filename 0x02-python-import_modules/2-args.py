"""
How to make a script dynamic!

Write a program that prints the number of and the list of its arguments.

The output should be:
Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
: (or . if no arguments were passed) followed by
a new line, followed by (if at least one argument),
one line per argument:
the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
Your code should not be executed when imported
The number of elements of argv can be retrieved by using: len(argv)
You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.
"""

#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """Prints the argument list passed to the program

    The program takes all the arguments starting from the second
    and prints the number of arguments and their value

    """
    av = sys.argv
    l_av = len(av) - 1

    if l_av > 1:
        print(l_av, 'arguments:')
        for i in range(1, l_av + 1):
            print('{:d}: {}'.format(i, av[i]))
    elif l_av == 1:
        print(l_av, 'argument:')
        for i in range(1, l_av + 1):
            print('{:d}: {}'.format(i, av[i]))
    elif l_av == 0:
        print(l_av, 'arguments.')
