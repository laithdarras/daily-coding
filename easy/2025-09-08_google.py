"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""

# What does "shift" mean here?
# Take the first char of A and move it to the end of A some number of time to the left. 
# Any number of times, including 0.
# So, abcde -> bcdea -> cdeab -> deabc -> eabcd -> abcde

# len(A) must be equal to len(B) for A to be shifted to get B! It can also be an empty string, but both have to be empty to be true.

# To approach this problem, we can create the rotation of A and check if B is in the rotation of A.
# We can do this by concatenating A with itself and checking if B is a substring of the result.
# Time complexity would be O(N) where N is len(A) going over each character in A once.
# Space complexity would be O(N) as well, since we are creating a new string that is twice the length of A.

# Edge cases: different lengths of A and B, empty strings, exactly the same strings, numeric strings, special characters.

# Rotation logic: (A[i:] + A[:i]) for i in range(len(A)): Check if B is in any of these rotations.

def shifted_string(A: str, B: str):
    # Base case
    if len(A) != len(B):
        return False

    # Rotation logic and check
    for i in range(len(A)):
        if A[i:] + A[:i] == B:
            return True
    return False

# test cases
print(shifted_string("abcde", "cdeab")) # True
print(shifted_string("abc", "acb")) # False
print(shifted_string(" ", " ")) # True
print(shifted_string("abcde", "abcd")) # False
print(shifted_string("abc", "abc"))     # True