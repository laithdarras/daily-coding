"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
"""

# UNDERSTAND
# Given a list and a pivot, I need to partition the list into three new lists (1 all vals less than pivot, 2 all vals equal to pivot, 3 all vals greater than pivot)
# Edge cases: empty list -> return 3 empty lists.
# negative numbers -> we take the absolute value of the number
# duplicates -> is fine
# one element in list -> return 1 list with that element and 2 empty lists

# MATCH
# This is a sliding window problem
# Three lists, one for each partition

# PLAN
# Initialize three empty lists
# Base case
# Iterate through original list
# List 1, append to list if less than pivot
# List 2, append to list if equal
# List 3, append to list if greater
# Return lists concatenated

# IMPLEMENT

def listPartition(pivot, lst):
    # Init
    less = []
    equal = []
    greater = []

    # base case
    if lst == []:
        return less, equal, greater
    
    # iterattion
    for i in lst:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            greater.append(i)

    return less + equal + greater

print(listPartition(10, [9, 12, 3, 5, 14, 10, 10]))

# EVALUATE
# time complexity would b O(N) since its iterating through the list once
# space also is O(3N) = O(N) since its creating 3 new lists
# pretty optimal solution, this was my brute force so glad i got it right
# maybe could do this problem in place with swapping so less space but would be more complex
# solution was good and efficient

# I knew this was a sliding window problem, I had the approach in my head since in my Computer Networks class we discussed the sliding window protocol yesterday hehe