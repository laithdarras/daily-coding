"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
"""

# Understand
# Space-efficient means in-place modification
# Most elements are zero, so we can use a dictionary to store only non-zero elements. 
# The dictionary will map indices to their corresponding non-zero values
# Edge cases: index out of bounds, setting a value to zero should remove it from the dictionary

# Match
# We can use a dictionary to store non-zero values and their indices for efficient space usage

# Plan
# We can create a class with the three methods

class SparseArray:

    def init(self, arr, size):
        self.size = size
        self.arr = {}
        for i in range(size):   # Check if element is not zero, then add to dictionary
            if arr[i] != 0:
                self.arr[i] = arr[i]

    def set(self, i, val):
        # BASE CASE
        if i < 0 or i >= self.size:
            return "Index out of bounds"
        # If value is zero, remove
        if val == 0:
            if i in self.arr:
                self.arr.pop(i) # Remove index from dictionary since value is 0
        else:
            self.arr[i] = val # Update value at curr index

    def get(self, i):
        if i < 0 or i >= self.size:
            return "Index out of bounds"
        return self.arr.get(i, 0) # Return value at index or 0 if not there

# Implement
test = SparseArray()
test.init([0, 0, 3, 0, 0, 5, 0], 7)
print(test.get(2))  # Output: 3
print(test.get(5))  # Output: 5
print(test.get(0))  # Output: 0
test.set(2, 0)     # Set index 2 to 0
print(test.get(2))  # Output: 0
test.set(1, 4)     # Set index 1 to 4
print(test.get(1))  # Output: 
print(test.arr) # Output: {5: 5, 1: 4}

# Review
# The code is working properly with an efficient space usage using a dictionary

# Evaluate
# Time complexity is O(1) for set and get operations
# Space complexity is O(1) for storing the hashmap, worst case is O(N) if all elements are non-zero since we have to store all elements in the hashmap