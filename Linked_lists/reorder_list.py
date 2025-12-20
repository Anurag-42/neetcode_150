# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # tortoise-hare algorithm to get the middle node via the slow pointer. 
        # reverse the half of linked list
        #merge them 

        # if not head or not head.next:
        #     return head

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next # middle node ptr
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None #cut the list to prevent the cycle while reversing 

        while curr != None:
            next_ptr = curr.next
            curr.next = prev
            prev = curr
            curr = next_ptr
        
        # prev is the reverse linked list's first node

        # Merging them now

        while prev != None:
            head_next = head.next
            prev_next = prev.next

            head.next = prev
            prev.next = head_next

            head = head_next
            prev = prev_next

        
        
        
        
        


        

    
