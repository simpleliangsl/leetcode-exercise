# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        
        if root == None: return []
        
        currentNodes = [root]
        result = []
        
        while len(currentNodes) > 0:
            tempNodes = []
            currentValues = []
            
            for node in currentNodes:
                currentValues.append(node.val)
                if node.left != None: tempNodes.append(node.left)
                if node.right != None: tempNodes.append(node.right)

            result.append(currentValues)
            currentNodes = tempNodes

        result.reverse()
        return result

    def test(self):
        root = TreeNode(1)
        result = self.levelOrderBottom(root)
        print(len(result))
