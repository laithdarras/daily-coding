"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
"""

# UNDERSTAND

# I need to reverse the order of words in a given string. Delimited by spaces is just fancy for words are separated by spaces.
# If letters in words are reversed, that's okay, I just need to reverse the order of words.
# words as in only between spaces, no punctuation or special characters mentioned.

# Example input: "hello world here" -> "here world hello". "byob is fun" -> "fun is byob"

# Edge cases: Empty string returns empty string. Single word returns same word. Multiple spaces between words should be reversed.
# Any spaces in the beginning or end of the string should be removed in the output, so only words separated by a single space will be in the final string

# MATCH
# This is a string manipulation problem.
# I can split the string into words, reverse the list of words, and then join them back together with spaces.

# PLAN
"""
1. Split input string by spaces to get a list of words
2. Reverse the list of words
3. Join the reversed list of words with a single space to return the final result
"""

def reverse_string(s: str):
    # Base case
    if not s:
        return s

    # split input string by spaces to get a list of words
    result = []
    words = s.split()

    # reverse the list of words
    for i in range(len(words) -1, -1, -1):      # this syntax (-1, -1, -1) means start at last index, go to index before 0, step backwards by 1
        result.append(words[i]) 

    # join reversed list of words with a single space
    return ' '.join(result)

    # return final string
    return result


# TEST
print(reverse_string("hello world here"))  # "here world hello"
print(reverse_string("byob is fun"))       # "fun is byob"
print(reverse_string(""))                   # ""
print(reverse_string("singleword"))        # "singleword"

# REFLECT
# My solution works well for the problem as stated.
# Time complexity is O(N) since we iterate through the string a few times (split, reverse, join) and NOT N^2 because each operation is linear.
# Space complexity is also O(N) since we create a new list of words and a new string for the result

# Follow-up: In-place reversal for mutable string representation
# I don't know how to do this in Python since strings are immutable. 