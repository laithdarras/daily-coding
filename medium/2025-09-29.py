"""
Good morning! Here's your coding interview problem for today.

Given a real number n, find the square root of n. For example, given n = 9, return 3.
"""

# UNDERSTAND
# This problem is just asking us to find the square root of a REAL number (not just an integer).
# This problem seems straightforward, but we need to consider edge cases like negative numbers and zero.
# Where negative is not defined in the REAL number system and zero is just zero.
# Still seems like a simple problem, not sure if there's a trick here since it was labeled as Medium difficulty.


# MATCH
# Well the square root of a number is just the number raised to the power of 1/2. So we can use the ** operator in python.
# this works for both ints and floats (real number system).
# Another option is to use the sqrt() function from the math library but that seems like overkill for this simple problem and also doesn't handle negative numbers i think


# PLAN
# Base case
# Exponentiation
# Return

# IMPLEMENT
def square_root(n):
    if n < 0:
        return None
    return n ** 0.5

print(square_root(9))  # 3.0
print(square_root(16))  # 4.0
print(square_root(2))  # 1.4142135623730951
print(square_root(0))  # 0.0
print(square_root(-4))  # None

# REVIEW
# Problem works for all real numbers

# EVALUATE
# Time and space complexity is both constant time since we're just doing a simple arithmetic operation.