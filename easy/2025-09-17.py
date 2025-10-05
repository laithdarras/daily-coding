"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a binary tree, return the level of the tree with minimum sum.
"""

# UNDERSTAND
# We need to traverse the tree level by level (BFS) and calculate the sum of each level
# We want the minimum sum and the corresponding level, so we need to keep track of both
# The input will be a list of a binary tree. The output will be the level with the minimum sum (2 ints)
# Edge cases: empty tree, root node only, negative values
# Assume the tree is valid and non-negative values

# MATCH
# Definitely gonna use BFS to traverse the tree level by level
# I also want to use a hashmap to store the sum of each level
# I can use a queue to help with the BFS traversal to process nodes level by level (FIFO)

# PLAN
# We first check if the tree is empty
# Then we initialize a queue with the root node and a variable to keep track of the current level (operations are O(1))
# Also a hashmap to store the sum of each level (since operations are O(1))
# Enter a while loop that continues until the queue is empty (meaning the tree is fully traversed)
# After traversing the tree, we find the level with the minimum sum in the hashmap and return it

# IMPLEMENT

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findSumAtLevel(root):

    # base case
    if not root:
        return None

    # queue for bfs
    treeQueue = deque()
    treeQueue.append(root) # this is to start bfs with root
    level = 0  # to keep track of level with min sum
    minSum = float('inf')
    minLevel = 0

    # traversal with bfs
    while treeQueue:
        size = len(treeQueue)  # Size is the number of nodes
        currSum = 0  # current level sum
        for _ in range(size):
            node = treeQueue.popleft() # FIFO to process nodes level by level
            currSum += node.val # add node value to currSum
            # Process children
            if node.left:
                treeQueue.append(node.left)
            if node.right:
                treeQueue.append(node.right)
        
        # After processing the level, check if currSum is less than minSum
        if currSum < minSum:
            minSum = currSum # update minSum
            minLevel  = level # update minLevel
        level += 1  # next level in tree
            
    return (minLevel, minSum)

# TEST
# One example for empty tree
print(findSumAtLevel(None)) # None

# One example for root only
print(findSumAtLevel(TreeNode(5))) # (0, 5)

# One example that L2 has the minimum sum
root = TreeNode(8)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(findSumAtLevel(root)) 

# Anyways, this problem took me too long to solve. I need to practice more tree problems. 
# This is NOT an easy problem like it was labeled. I struggled with the BFS traversal and keeping track of the sums
# Time complexity is O(N) where N is the # of nodes in the tree because we visit each node once.
# It could be O(LOGN) if the tree is balanced, but in the worst case (unbalanced) it is O(N)

# Will practice more problems involving trees and BFS traversal. I can't believe this is labeled as easy.
# Adios amigos
