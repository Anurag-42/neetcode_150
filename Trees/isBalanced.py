# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.res = True

        def helper(node):
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)

            self.res = self.res and (abs(left - right) < 2)

            return 1 + max(left, right)

        helper(root)
        return self.res
