#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculate the factorial of a given number recursively.

    Parameters:
    - n (int): The number whose factorial is to be calculated.

    Returns:
    - int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input argument from the command line
# and calculate its factorial using the factorial function
f = factorial(int(sys.argv[1]))

# Print the factorial
print(f)

