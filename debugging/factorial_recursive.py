#!/usr/bin/python3
import sys

# Function Description: This function calculates the factorial of a number recursively.
# Parameters: n (int) - The number for which the factorial is to be calculated.
# Returns: The factorial of the number 'n'.
def factorial(n):
    # Base case: if n is 0, return 1 (since the factorial of 0 is 1)
    if n == 0:
        return 1
    else:
        # Recursive case: return n multiplied by the factorial of (n-1)
        return n * factorial(n-1)

# Convert the first command line argument to an integer and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)