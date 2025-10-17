"""
Good morning! Here's your coding interview problem for today.

This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:

   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
"""

# UNDERSTAND
# Tree with nodes 0 or 1. Need to kill all subtrees that are 0s. Straighforward tree traversal problem
# Edge cases: empty tree -> return none. root only 0 -> return none. root only 1 -> return root
# tree with all 0s -> return none. tree with all 1s -> return tree
# ofc mix of 0s and 1s return pruned tree

# MATCH#
# tree traversal problem -> can use dfs or bfs. 
# if need to modify tree structure, dfs is better because we can go to the leaf nodes first
# I will kill any 0s using DFS using post order traversal in order to kill the leaf nodes the fastest

# PLAN
# TreeNode class
# main function that takes root node
# DFS function that returns true if subtree has 1, false if all 0s
# call dfs on children since im using post order
# if left child is false, set left to none since its a 0
# if right is false, set right to none
# after checking children, return true if current node is 1 or if left or right is true
# if dfs is false then there are no 1s in the tree, return none

# IMPLEMENT

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode({self.value})"
    
    def __repr__(self):
        return f"TreeNode({self.value})"


def kill_zeros(root):
    # base case
    if not root:
        return None

    # dfs
    def dfs(root):
        if not root:
            return False

        left = dfs(root.left)
        right = dfs(root.right)

        if not left:
            root.left = None
        if not right:
            root.right = None

        if (root.value == 1) or left or right:
            return True
        
        return False
    
    next = dfs(root)

    if not next:
        return None
    
    return root

# TEST
def print_tree(node, prefix=""):
    if not node:
        print(prefix + "None")
        return
    print(prefix + str(node.value))
    # only descend if there's something to show
    if node.left or node.right:
        print_tree(node.left, prefix + "L-")
        print_tree(node.right, prefix + "R-")

print("Test")
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(0)
root.right.left.left = TreeNode(0)
root.right.left.right = TreeNode(0)

pruned = kill_zeros(root)
if pruned is None:
    print("None")
else:
    print_tree(pruned)

# I need practice with tree traversal problems.
# It always outputs the memory address instead of the tree structure. Something with my printing method i think

# Added a print tree function since it gave me problems just printing the actual tree
# Time complexity is O(N) since we visit each node once
# Space complexity is O(H) where H is the height of the tree due to recursion
# I ended up using post order traversal but called root first since I needed to modify the children before the parent
# Tree problems are fun but i need more practice