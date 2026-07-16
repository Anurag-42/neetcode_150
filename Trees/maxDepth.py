# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_depth = 0
        if root is None:
            return max_depth
        else:
            left_max_depth = self.maxDepth(root.left) + 1
            right_max_depth = self.maxDepth(root.right) + 1
            return max(left_max_depth, right_max_depth)
        
'''

The algorithm visits each node exactly once, so the time complexity is O(N).
The auxiliary space is determined by the recursion stack, which is O(H) where H is the tree height
O(log N) for a balanced tree and O(N) in the worst case for a skewed tree.

space complexity is not the total number of recursive calls—it is the maximum number of calls on the stack at the same time.

'''
