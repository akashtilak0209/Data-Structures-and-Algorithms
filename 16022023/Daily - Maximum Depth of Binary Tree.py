# Question 104: Daily - Maximum Depth of Binary tree: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Approach:
"""Learned the concept of Binary Tree from Shubham. Preorder, Postorder, In-order Traversal methods.
Preorder: NLR
Postorder: LRN
Inorder: LNR

For this traversal, I used Recursion and returned 0 whenever the node returned None.
Took maximum of return from left and right node and added 1 to it to get the depth of the Binary tree.
Also learnt about initialising binary tree using constructor in an object in IDE.
"""

# Class TreeNode for constructor of an object:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution:(Brute Force)
def mySolution(root):
    if root == None:
        return 0
    l = mySolution(root.left)
    r = mySolution(root.right)
    return (max(l, r) + 1)

def mySolution2():
    pass

# Error(if any):
""""""

# Optimized Solution:
def myOptimizedSolution():
    pass

# Original Solution:
def originalSolution(root):
    return 0 if root == None else 1 + max ( originalSolution(root.left) , originalSolution(root.right) )

# Mistake(Difference):
"""
One liner ternary operator used.
Space of l and r saved.
"""

# Note/Concept:
"""
Learn using root and binary tree implementation in sending arguments, nodes and root.
"""

# Solution Execution:
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(9)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)


    print(f"My first solution: {mySolution(root)}")
    # print(f"My second solution: {mySolution2()}")
    # print(f"My optimized solution: {myOptimizedSolution()}")
    print(f"Original solution: {originalSolution(root)}")