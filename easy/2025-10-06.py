"""
Good morning! Here's your coding interview problem for today.

This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
"""

# UNDERSTAND
# This problem asks me to find the minimum path sum from root to leaf
# In a binary tree, a path is the root node to a leaf node following the connections down the tree

# MATCH
# This requires a tree traversal algorithm DFS
# Recursively traverse the tree using DFS and keeping track of the current path sum

# PLAN
# Base Case of No tree (return 0)

# Recursively traverse using DFS

# Add current node value to result sum


# If it is a leaf node (no children), return current path sum

# compare path sums from left and right subtrees and return minimum

# IMPLEMENT
# Define tree node class
class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def dfs(node, curr):
    if not node:
        return None
    
    curr += node.value # Add current node value to result sum for min path sum
    print(curr)

    # If leaf, return sum
    if not node.left and not node.right:
        return curr
    
    # Traverse
    left = dfs(node.left, curr)
    right = dfs(node.right, curr)
    print(left, right)

def findMin(root, left, right):
    # Base case
    if not root:
        return 0

    # DFS
    dfs(root, 0)
    print(left, right)

    # Compare
    if left is None:
        return right
    else:
        return min(left, right)


print(findMin(TreeNode(10, TreeNode(5, TreeNode(1, TreeNode(-1, None, None), None), None), None), None, None)) # 15

# REVIEW
# I could not finish this problem in the time allotted I gave myself (which was 30 minutes to mimick a real interview). 
# I was able to identify the correct approach, but I struggled with the implementation
# It was correctly printing the current path sums, but DFS was not returning the correct values to compare
# It kept on returning None, even though I had a base case for leaf nodes and I also had DFS being called on both left and right children
# I need to review tree traversal algorithms and practice on implementing them correctly

# EVALUATE
# If this was solved correctly, my approach would have a time complexity of O(LOG N) where N is the # of nodes in the tree 
# DFS would visit each node once and because it is a tree the height would be LOG N in a balanced tree
# Space complexity is O(H) where H is the height of the tree from recursively storing function calss on the stack