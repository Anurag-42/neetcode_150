# Reverse a singly linked list

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Iterative implementation
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev_ptr = None
        curr_ptr = head
        #O(1) space and O(n) time
        while curr_ptr != None:
            next_ptr = curr_ptr.next 
            # I have all 3 ptr for the node of interest currently

            #Now
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr

            #change the node
            curr_ptr = next_ptr

        return prev_ptr
            

# tail recursive implementation
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.helper(head, None)

    def helper(self, curr, prev=None):
        #No tail call optimization so O(n) space complexity
        if not curr:
            return prev
        next_node = curr.next
        curr.next = prev
        return self.helper(next_node, curr) 

