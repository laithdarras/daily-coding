"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""
# UNDERSTAND THE PROBLEM
# We need to return a lift of lists, where each list represents a path from the root to a leaf node in the binary tree.
# Leaf node is one that does't not have any children nodes
# Output is a list of lists, order doesn't matter but try exploring left to right
# Input is a binary tree which is a list of nodes where each node has a value and pointers to left and right children

# Edge cases: empty tree --> return empty list. only root node --> return list with only root node value. unbalanced tree --> still need to explore all paths. duplicate values --> still needs to work

# MATCH
# DFS is screaming at me here, and we use a stack to keep track of the current path since it is LIFO
# Recursion and interation both work here, but recursion might be cleaner so we will go with that

# When we reach a leaf node, we add the current path to the result list

# PLAN
# Base case: if empty tree, return empty list
# initialize result list to store all paths and current path list to store the current path
# write dfs func that takes a node as input
    # add the node's value to the current path
    # if the node is a leaf, append the current path to the result
    # else, call dfs on left and right (if they exist)
    # why do we need to backtrack? because we need to remove the last node from the current path when we return from the recursive call to explore other paths
    # call dfs on root

# return result

# IMPLEMENT
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def all_paths(root):
    # Base case
    if not root:
        return []

    result = []
    curr = []

    def dfs(node):
        if not node:
            return None

        curr.append(node.key)

        if not node.left and not node.right:
            result.append(curr[:]) # append a copy of curr to result. what is [:]? it is a slice that creates a shallow copy of the list

        else:
            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)
        
        curr.pop()

    dfs(root)

    return result

# TEST

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
print(all_paths(root)) # [[1, 2], [1, 3, 4], [1, 3, 5]]

root = None
print(all_paths(root)) # []

# EVALUATE
# Time complexity: O(N) because we visit each node once
# Space complexity: O(H) for the height of the tree

# This can be O(LOGN) for balanced tree (best case) and O(N) for unbalanced tree (worst case).