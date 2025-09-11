"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

# UNDERSTAND
# We need to find all starting indices in the string where an anagram of the word starts

# Anagram: A word formed by rearranging the letters of another, "silent" is an anagram of "listen"
# It is NOT the same thing as a palindrome!

# Example input: W = "ab", S = "abxaba" --> Output: [0,3,4] because "ab", "ba", and "ab" are anagrams of "ab"
# Example input: W = "abc", S = "cbadefabc" --> Output: [0,6] because "cba" and "abc" are anagrams of "abc"
# Example input: W = "a", S = "aaaaa" --> Output: [0,1,2,3,4] because every character is an anagram of "a"
# Example input: W = "xyz", S = "abcdef" --> Output: [] because there are no anagrams of "xyz" in "abcdef"

# Input constraints: W and S are non-empty strings, len(W) <= len(S), lowercase letters only, no spaces or special chars
# Output: list of starting indices of anagrams of W in S in ascending order (0-indexed)

# Edge cases: Empty strings, W longer than S, no anagrams found, all chars in W are the same, single chars in both

# Assume input is valid

# MATCH
# String manipulation problem. We can use a sliding window approach to check each substring of S with length <= W
# We store the the character counts of W in a hashmap and compare it with the character counts of each substring of S
# If they match, we add the current starting index to the result list and return that list at the end

# PLAN
# Create a function that takes W and S as inputs
# Create 2 hashmaps to store character counts of W and the current window in S
# Initialize the first window in S and add its index if it matches W's counts
# Slide the window across S, updating counts and checking for matches
# Return the list of indices

# IMPLEMENT

from collections import defaultdict # this is the dictionary import required

def find_anagram_indices(W, S):
    
    # Base case
    if len(W) > len(S):
        return []   # it cannot be possible to have an anagram if W is longer than S
    
    # hashmap time baby
    w_count = {}
    s_count = {}

    # initialize the character counts for W and the first window in S
    for i in range(len(W)):
        w_count[W[i]] = w_count.get(W[i], 0) + 1    # this is how we count characters in W
        s_count[S[i]] = s_count.get(S[i], 0) + 1   # this is how we count characters in the first window of S
    
    result = []     # this will store the starting indices of anagrams

    # check if the first window is an anagram
    if w_count == s_count:  # if the character counts match, then we have an anagram
        result.append(i - len(W) + 1) # i - len(W) + 1 can also be written as 0, since i is len(W) - 1 at this point
    
    # slide the window across S
    for i in range(len(W), len(S)):
        
        # Add the new character to the current window to keep track of counts
        s_count[S[i]] = s_count.get(S[i], 0) + 1

        # Then, we remove the char that is sliding out of the window
        idx = i - len(W)
        s_count[S[idx]] -= 1

        # If the count of that char becomes 0, we remove it from the hashmap because it is no longer in the window
        if s_count[S[idx]] == 0:
            s_count.pop(S[idx])

        # Check if current window is anagram and add starting index to result if it is
        if w_count == s_count:
            result.append(i - len(W) + 1)
        
    # Return the result list
    return result

# TEST
print(find_anagram_indices("ab", "abxaba")) # Output: [0, 3, 4]
print(find_anagram_indices("abc", "cbadefabc")) # Output: [0, 6]
print(find_anagram_indices("a", "aaaaa")) # Output: [0, 1, 2, 3, 4]
print(find_anagram_indices("xyz", "abcdef")) # Output: []

# EVALUATE
# Time complexity would be O(N) best case and O(NM) worst case where N is the length of S and M is the length of W
# This is because we are iterating through S once and for each window, we are comparing the two hashmaps which takes O(M) time in the worst case which is when all characters are different

# Space complexity is O(1) because the size of the hashmaps is limited to the number of different characters in the strings, which is at most 26 for lowercase letters

# This was a tough problem, but I think the sliding window approach is efficient and works well for this problem.
# The use of hashmaps to store char counts is good for quick comparison since KV lookups are O(1)

# I'm not sure how to optimize the hashmap comparison further, but this solution should work well for most cases

# Hard problem, but I think i did well :)