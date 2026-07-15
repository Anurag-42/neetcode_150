# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' In an array based representation, parent -> n, left/right -> 2n+1/2n+2 '''
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left
        # one of the nicest features in Python
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        