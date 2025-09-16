"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
"""

# UNDERSTAND
# This is very vague. We can interpret it in a few ways:
# First, we can generate a binary tree with a random number of nodes each time
# Or we can generate a tree with a fixed number of nodes but with random values
# Or even we can generate a tree with a fixed structure (left and right evenly) but with random values

# The problem states "arbitrarily large" which could mean that the tree can grow as large as needed
# But it also states "finite" which means we can't have an infinite tree
# It needs to run in O(1) time, which means we can't traverse the tree in the original sense bc that would take O(n) time

# Edge cases:
# Tree with 0 nodes - return None. Tree with root only - return root. Tree with left and right children - return root with left and right children. 
# Tree with left child only - return root with left child and same thing for right child only

# MATCH
# An algorithm in mind is to use a random number generator to decide the size of the tree
# Call the function recursively to build the tree, but this would take O(N) time

# Let's go with the O(N) approach first, then I'll think about how to optimize it to constant time

import random as rand

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        # Print tree as nested lists of values for simplicity
        return str(self.to_list())

    def to_list(self):
        # Preorder traversal as nested lists
        if self.left is None and self.right is None:
            return self.value
        return [self.value,
                self.left.to_list() if self.left else None,
                self.right.to_list() if self.right else None]

def generate(numNodes=None) -> TreeNode:
    # If numNodes is None, pick a random size
    if numNodes is None:
        numNodes = rand.randint(1, 100)  # Arbitrarily large but finite

    if numNodes == 0:
        return None

    root = TreeNode(rand.randint(0, 100))
    if numNodes == 1:
        return root

    # Randomly split remaining nodes between left and right
    left_nodes = rand.randint(0, numNodes - 1)
    right_nodes = numNodes - 1 - left_nodes

    root.left = generate(left_nodes)
    root.right = generate(right_nodes)
    return root
# TEST
# Test cases:
print(generate())   # Random tree
print(generate(1)) # TreeNode with random value
print(generate(3)) # TreeNode with left and right children
print(generate)   # None
print(generate(1)) # TreeNode with random value
print(generate(3)) # TreeNode with left and right children