"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

# UNDERSTAND
# I need to find the first letter that appears more than once in the string
# Not the total letters, but the first one that shows up again
# This makes it easier bc I can stop as soon as I find the first one
# Edge cases: if empty string --> return Null, if no recurring characters --> return None
# if all characters are the same --> return that character
# assume all characters are lowercase a-z

# MATCH
# String manipulation problem
# I can use a hashmap or a set
# Will use a set since its easier for counting unique items

# PLAN
# base case
# Create an empty set
# Loop through string
# If it's in the set, return it
# that's it folks

# IMPLEMENT

def findFirstRecurringChar(str):
    seen = set()

    for char in str:
        if char in seen:
            return char
        seen.add(char)
    
    return None

print(findFirstRecurringChar("acbbac"))  # b
print(findFirstRecurringChar("abcdef"))  # None
print(findFirstRecurringChar(""))  # Null

# Sets are so awesome since it handles uniqueness for us
# all i gotta do is check if its there or not
# if it is, return it
# if not, add it to the set
# super simple and efficient. it runs in O(N) time and O(N) space since i'm looping through string once

# String problems are fun