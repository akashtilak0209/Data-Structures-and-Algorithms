# Question 783: Minimum Distance Between BST Nodes : https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Approach:
""""""

# Class TreeNode for constructor of an object:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution:(Brute Force)
def mySolution(root):
    def my(root, mini):
        if root == None:
            return 0

        l = my(root.left, mini)
        r = my(root.right, mini)
        small = min(root.val-l,abs(root.val-r))
        if small!=0:
            mini.append(small)
        print(mini)
        return root.val
    mini=[]
    my(root,mini)
    return min(mini)

def mySolution2():
    pass

# Error(if any):
""""""

# Optimized Solution:
def myOptimizedSolution():
    pass

# Original Solution:
def originalSolution():
    pass

# Mistake(Difference):
""""""

# Note/Concept:
""""""

# Solution Execution:
if __name__ == '__main__':
    root = TreeNode(71)
    root.left = TreeNode(62)
    root.right = TreeNode(84)
    root.left.left = TreeNode(14)
    root.right.right = TreeNode(88)

    print(f"My first solution: {mySolution(root)}")
    print(f"My second solution: {mySolution2()}")
    print(f"My optimized solution: {myOptimizedSolution()}")
    print(f"Original solution: {originalSolution()}")