# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, tree1, tree2):
        if tree1 == None or tree2 == None:
            return tree1 == tree2
        else:
            return tree1.val == tree2.val and \
                   self.isMirror(tree1.left, tree2.right) and \
                   self.isMirror(tree1.right, tree2.left)

class SolutionTest:
    def 
