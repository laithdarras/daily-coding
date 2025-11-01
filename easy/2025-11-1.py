"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.
"""

# UNDERSTAND
# Bit manipulation!
# I need to do 1s complement of the 32 bit int
# Edge cases: if no bits, return 0. 

# Problm will only be 1 or 0s

# MATCH
# bit manipulation
# i will need to do 1s complement by flipping each bit using the ~ symbol which is the NOT operator

# PLAN
# Base case
# Then flip the bits
# then return
# simple as that

# def bitsReversed(n):
#     # treat input as 32-bit unsigned
#     result = ""

#     for i in range(32):
#         if i == "0":
#             result += "1"
#         else:
#             result += "0"
    
#     return result
# print(bitsReversed(0b11110000111100001111000011110000))

# this approach is clearly not working, ill just use the bitwise operations

def bitwiseReverse(n):

    result = 0
    for i in range(32):
        nextBit = (n >> i) & 1 # i use the right shift operator to to shift the bits to the right by i position and then use the AND operator to get the last bit in order 

        result |= (nextBit << (31 - i)) # OR operator to set the bit at the reversed position in the result and subtract i from 31 to get the 32 bit reverse pisition with a left shift operator to bring  the bit to the correct position

    return result

# Print as a 32-bit binary string with leading zeros
print('0b' + format(bitwiseReverse(0b11110000111100001111000011110000), '032b'))  # Output: 0b00001111000011110000111100001111

# this works now. this took me so long to figure out over an hour
# bit manipulation is super interesting but difficult
# NOT an easy problem at all, not sure why it was labeled easy

# time complexity is O(1) since were always doing only 32 iterations never n iterations