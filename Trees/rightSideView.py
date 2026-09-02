# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        '''
        essentially getting the right most element of each level

        '''
        res = []
        if not root:
            return []
        curr_level = [root]
        
        while curr_level:
            next_level = []
            tmp = []

            for i in range(len(curr_level)):
                node = curr_level[i]
                tmp.append(node.val)
            
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            

            res.append(tmp[-1])
            curr_level = next_level
            next_level = []  
            tmp = []

        return res
