"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Cisco.

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""

# Unsigned means non-negative
# We want to swap adjacent bits
# So 0b10101010 -> 0b01010101
# And 0b 11110000 -> 0b11110000
# And 0b11000101 -> 0b11001010

# Let's understand the 8 but integer positions:
# Bit positions: 7 6 5 4 3 2 1 0
# Example:       1 0 1 0 1 0 1 0
# We want to swap (7,6), (5,4), (3,2), (1,0)

# We use bitwise operations to achieve this (ie AND, OR, SHIFT)

# To isolate even bits, we can use the mask 0b10101010 (0xAA in hex)
# To isolate odd bits, we can use the mask 0b01010101 (0x55 in hex)

# We shift the even bits right by 1 and the odd bits left by 1, using the << and >> operators

# So we can use (n & 0xAA) >> 1 to get the even bits shifted right and (n & 0x55) << 1 to get the odd bits shifted left

# Final operation would be to combine these two with the OR operator

# Edge cases: 0b00000000 -> 0b00000000 (same) and 0b11111111 -> 0b11111111 (same) and 0b00000001 -> 0b00000010 (swapped)

# Solution:
def swap_bits(n: int):

    even = (n & 0xAA) >> 1
    odd = (n & 0x55) << 1
    return even | odd
    # return ((n & 0xFF) << 1) | ((n & 0xAA) >> 1)

# Test cases
print(bin(swap_bits(0b10101010))) # Expected: 0b01010101
print(bin(swap_bits(0b11100010))) # Expected: 0b11010001

# Time complexity: O(1) since we are doing a constant number of operations throughout regardless of input size
# Space complexity: O(1) since we are using a constant amount of space