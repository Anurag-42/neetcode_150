# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#return height (helper function) (upside down)
# update diameter (global var) (downward up)
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            # Update the largest diameter found so far
            self.diameter = max(self.diameter, left + right)

            # Return height of this subtree
            return 1 + max(left, right)

        height(root)
        return self.diameter
