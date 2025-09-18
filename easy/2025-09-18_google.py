"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""

# UNDERSTAND
# I need to square each element in the sorted list and return the same list in sorted order
# The input is a sorted list of ints (can be -/+/0) and the output is a sorted list of squared ints
# Edge cases:
# empty list -> return None
# list with one element -> return the square of that element
# list with all negative elements -> return the squares in reverse order because squaring neg makes pos
# list with all positive elements -> return squares in same order
# list with mix -> need to find the point where neg becomes pos and then merge two sorted lists

# MATCH
# I thought about using in-place modification but that would mess up the order because of neg numbers and would take up O(nlogn) time to sort again
# A faster approach would be to use two pointers technique to merge two sorted lists. 
# One pointer at the start (for neg numbers) and one at the end (for pos)
# I can then compare the squares of the elements at these pointers and add the larger one to the result list, moving inwards until no more to compare
# This is O(N) where N is num of elements in list and O(N) space for the new list

# PLAN
# Initialize two pointers, left at start (0) and right at end (len(list)-1)
# Initialize result list
# Make a while loop that runs until left pointer meets right pointer
# Inside the loop, compare the squares of elements and append the larger one to the result
# Return the list

# IMPLEMENT

def sortTheSquares(arr):
    
    # base case
    if not arr:
        return None

    # init ptrs/result
    left = 0
    right = len(arr) -1
    result = []


    # loop until ptrs meet
    while left <= right:
        
        # calc the squares
        leftSq = arr[left] ** 2
        rightSq = arr[right] ** 2

        # compare and append larger to result and move inward
        if leftSq > rightSq:
            result.append(leftSq)
            left += 1
        else:
            result.append(rightSq)
            right -= 1

    return result[::-1] # reverse result instead of sorting again since we know it's in descending order

# REVIEW
print(sortTheSquares([-9, -2, 0, 2, 3])) # [0, 4, 4, 9, 81]
print(sortTheSquares([])) # None
print(sortTheSquares([-3])) # [9]
print(sortTheSquares([4])) # [16]

# EVALUATE
# O(N) time AND space complexity where N is the elements in the list.
# I traverse the list once and create a new list of same size

# My first thought on in-place would have been O(NLOGN) time because of the need to sort again
# Here we just reverse the list because we know it will be in descending order due to the two pointer approach

# Good approach overall I think with two pointers. Arrays are good for problems where you need to access elements by index
# And two pointers is good for sorted arrays where you need to compare elements from both ends or find pairs that meet a certain condition
# More practice with arrays is needed though