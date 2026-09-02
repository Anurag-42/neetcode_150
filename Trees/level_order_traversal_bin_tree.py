# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        '''
        
        1. Take all nodes belonging to CURRENT level
        2. Create an empty collection for NEXT level
        3. Process every node in CURRENT
        4. While processing them, add their children to NEXT
        5. CURRENT = NEXT
        6. Repeat'''


        res = []
        
        if not root:
            return res

        curr_level = [root]
        next_level = []
        temp = []

        while curr_level:
            
            temp.append(curr_level[0].val)
            left,right = curr_level[0].left, curr_level[0].right
            # a = a.append(b) makes a None
            if left:
                next_level.append(left)
            if right:
                next_level.append(right)
            curr_level = curr_level[1:]
            if len(curr_level) > 0:
                continue
            else:
                curr_level = next_level
                next_level = list()
                res.append(temp)
                temp = list()
        return res

        



            
