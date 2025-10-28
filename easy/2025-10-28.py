"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. 
daily should return false, since there's no rearrangement that can form a palindrome.
"""

# UNDERSTAND
# A palindrome is a string that is the same both forwards and backwards
# A permutation is any rearrangement of the letters in the string, so it doesn't have to be just reversing the string
# Edge cases: empty string -> return None, single character string -> return True
# if the length of the strings are different -> return false
# if the string has an even length, write an algorithm that checks if all characters have even counts

# MATCH
# HASHMAP TIME BABY WOOHOOO!
# Use a hashmap to have the key be the letter and the value be the count of that letter
# Use it to check if the counts of the letters are even or odd

# PLAN
# create the hashmap
# iterate through the string and add the counts to the hashmap
# check the counts 
# return conditions

# IMPLEMENT

def isPalindrome(string):
    # Base case
    if len(string) == 0:
        return None
    if len(string) == 1:
        return True
    

    # hashmap
    counts = {}

    # loop
    for char in string:
        if char in counts:   # check if the key is already in the hashmap
            counts[char] += 1 # increment the count
        else:
            counts[char] = 1 # only letter in the string so far


    # check
    count = 0
    for key in counts:
        if counts[key] % 2 == 0:
            continue # If it's even, keep going because it's a palindrome
        else:
            count += 1 # increment count of odd letters to keep checking 
            if count > 1: # If there's more than one different letter with an odd count, it's not a palindrome
                return False
    
    # return
    return True

print(isPalindrome("carrace")) # True
print(isPalindrome("daily")) # False

# My solutions works and it runs in O(N) time because it loop through the string once
# and then loops through the hashmap which in the worst case is O(N). best case is O(1) if all characters are the same.
# space complexity is O(1) because the hashmap will only have a max of a fixed number of chars

# Hashmaps are great for counting occurrences of items, but so are sets
# Let me do this using a set

def setVersion(string):
    if len(string) == 0:
        return None
    if len(string) == 1:
        return True
    
    mySet = set()

    for char in string:
        if char in mySet:
            mySet.remove(char)
        else:
            mySet.add(char)
    
    return len(mySet) <= 1

print(setVersion("carrace")) # True
print(setVersion("daily")) # False

# Simpler code because sets are built to handle unique items
# We remove characters that we see again, because that means it is a palindrome candidate.
# Add characters to the set if we see them for the first time since it might not be a palindrom
# If the lenght of the set is <= 1, it's a palindrome because each character needs to have an even count except for at most one character
# Same time and space complexity but simpler code