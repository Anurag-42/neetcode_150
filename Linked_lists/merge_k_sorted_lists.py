# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Idea is to just merge 2 first linked lists of list of linked list at a time
#O(N*K) time and O(1) space
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        len_lists = len(lists)
        if len_lists== 0:
            return None
        if len_lists == 1:
            return lists[0]
        x = self.helper(lists[0], lists[1])
        for i in range(2, len_lists):
            x = self.helper(x, lists[i])
        return x

    #merges 2 lists O(n) time O(1) space where n is the biggest list
    def helper(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        # At this point, none are NULL ptrs

        head = list1 if list1.val <= list2.val else list2
        if head == list1:
            curr_first = list1.next
            curr_second = list2
        else:
            curr_first = list1
            curr_second = list2.next

        temp = head
        while curr_first and curr_second:
            curr_first_val = curr_first.val
            curr_second_val = curr_second.val

            if curr_second_val <= curr_first_val:
                temp.next = curr_second
                temp = temp.next
                curr_second = curr_second.next
            else:
                temp.next = curr_first
                temp = temp.next
                curr_first = curr_first.next
        
        if curr_first:
            temp.next = curr_first
        if curr_second:
            temp.next = curr_second
        return head
           
            

            

            
            

        
        
                
            
