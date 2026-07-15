# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.best = float('-inf')

        #moving down the tree while thinking up in dfs

        def dfs(root): #which path can my parent take if there was a parent above me
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            curr = root.val

            # Ignore negative paths
            left = max(0, left)
            right = max(0, right)

            opt4 = left + curr
            opt5 = right + curr
            opt6 = left + curr + right

            # This path ends here, so update the overall answer
            self.best = max(self.best, curr, opt4, opt5, opt6)

            # Return only a path that the parent can continue
            return max(opt4, opt5)

        dfs(root)
        return self.best


