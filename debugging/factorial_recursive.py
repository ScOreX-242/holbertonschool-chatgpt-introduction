#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given integer.

    Function Description:
    ---------------------
    Computes the factorial of a non-negative integer by recursively multiplying it with all positive integers less than itself.

    Parameters:
    -----------
    n : int
        The non-negative integer for which the factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of the input integer n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Usage: ./factorial_recursive.py <number>")
    sys.exit(1)

try:
    # Retrieve the integer input from command-line argument
    f = factorial(int(sys.argv[1]))
    # Print the factorial result
    print(f)
except ValueError as e:
    print("Error: {}".format(e))
    sys.exit(1)
