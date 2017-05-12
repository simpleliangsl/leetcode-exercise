# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return sumN(self, 0, root)

    def sumN(self, parentSum, tree):
        if tree == None:
            return parentSum
        
        parentSum = parentSum*10 + tree.value
        return sumNumbers(self, parentSum, tree.left) + \
               sumNumbers(self, parentSum, tree.right)
