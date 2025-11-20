"""
Write a function that removes duplicates from an array. 
The function should take an array as input and return a new array with all duplicate elements removed. 
"""

# This function will return a new array with no duplicates in it
# If there is a duplicate element, remove just one of them
# Assume lowercase strings only allowed in the array

# Use a set or a hashmap to count the duplicates
# The set will be easiest since it's purpose is to return only unique items in an array
# A set itself cannot contain duplicates so this will be straightforward

def removeDuplicates(arr):
    # Base case
    if arr is None:
        return -1
    newArr = list(set(arr))
    print(f"Original list: {arr}")
    print(f"New list: {newArr}")

print(removeDuplicates(["Hello", "Bye", "Hello", "Water", "Laptop", "Water"]))

# Relational algebra is super neat :>)