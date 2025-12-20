# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#O(n) time and O(1) space
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        '''nth node from end of list => len(list) - n index starting from 0 if
        we look from the beginning'''

        
        # Finding length of linked list
        curr = head
        len_ll = 0

        while curr != None:
            len_ll += 1
            curr = curr.next
        if len_ll == 1:
            return None
        required_index = len_ll - n
        # Edge Case
        if required_index == 0:
            head = head.next
            return head

        curr_ptr = head
        ctr = 0
        prev_ptr = None

        while curr_ptr != None:
            next_ptr = curr_ptr.next
            if ctr == required_index:
                prev_ptr.next = next_ptr
            else:
                prev_ptr = curr_ptr
            
            ctr += 1
            curr_ptr = next_ptr
        return head
        
        
                
        
        
