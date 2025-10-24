"""
Good morning! Here's your coding interview problem for today.

Find an efficient algorithm to find the smallest distance (measured in number of words) between 
any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world", 
return 1 because there's only one word "cat" in between the two words.
"""

# UNDERSTAND
# This is an interesting problem
# I need to find the smallest distance between two words in a string
# That "distance" is measured in number of words between them
# Words will be denoted by spaces so for example a letter will be a word if it's separated by spaces
# Edge cases: if the list is empty, I need to return -1 and not None bc I need to save return None for when 
# one or both of the words are not in the list. Another case is when the two words are the same,
# in which I need to find the smallest distance between those two same words
# another case is when the list is shorter than 2 words, return -1
# I need to come up with a space and time efficient solution

# MATCH
# String manipulation!
# I can use a hashmap to store how many times each words appears in the list
# Then to use the two pointer technique to look at the start and end of the list and move them closer
# If I find one of the words, add it to the hashmap to store the word with its index
# Keep doing that until the algorithm converges
# Then I want to check the hashmap for the two words and calculate the distance by subtracting their indices
# Need to keep track of minimum distance found so far
# Then I will return that minimum distance
# but wait, I shouldn't just subtract the indices, I need to subtract and then minus 1 to get the number of words in between
# Now I can implement

# PLAN
# 1. Split the string into a list of words
# 2. Initialize two pointers
# 3. Initialize my hashmap
# 4. Use a while loop to move the pointers closer, adding words to the hashmap
# 5. Check hashmap for the two owrds and calculate distance
# 6. Keep track of minimum
# 7. Return that one

def findMinDistance(text, wordA, wordB):
    # 1
    words = text.split()

    # Base case
    if len(words) < 2:
        return -1
    
    # 2
    left = 0
    right = len(words) -1

    # 3
    hashmap = {}

    # 4
    while left <= right:
        if words[left] == wordA or words[left] == wordB:
            hashmap[words[left]] = left 
        elif words[right] == wordA or words[right] == wordB:
            hashmap[words[right]] = right
        
        left += 1
        right -= 1
    
    # 5
    if wordA not in hashmap or wordB not in hashmap:
        return None
    
    # 6
    for key in hashmap:
        if key == wordA:
            indexA = hashmap[key]
        elif key == wordB:
            indexB = hashmap[key]
    
    minDist = abs(indexA - indexB) - 1 # distance is positive

    return minDist

test = "dog cat hello cat dog dog hello cat world"
print(findMinDistance(test, "hello", "world"))

# Evalulate
# I tried to solve this problem with my algorithm, it doesn't work
# after debugging, I realized that my algorithm doesn't work for two reasosn:
# 1. single distance calculation and doesn't check for other possible distances
# 2. my while loop seems t be overwriting previous indices because im storing something everytime a word is found which overwrites the previous index
# My intuition was correct about using two pointers, but I needed to change my approach
# Instead of scanning from both ends, I should scan the lists from start to end with a single pointer
# and then use the second pointer to keep track of the last seen index of each word
# then i can calculate the distance each time i find one of the words
# and update the minimum distance if it's smaller than the previous one