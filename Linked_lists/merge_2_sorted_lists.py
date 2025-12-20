# Definition for singly-linked list.
#O(n+m) space and time. Time obv; Space because no stack optimization for recursion
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # No need for prev because not interested in reversing
        if not list1:
            return list2
        if not list2:
            return list1
        
        # At this point, none are NULL ptrs

        curr_first_val = list1.val
        curr_second_val = list2.val

        if curr_first_val <= curr_second_val:
            rem_sorted_merged_list = self.mergeTwoLists(list1.next, list2)
            list1.next = rem_sorted_merged_list
            return list1

        else:
            rem_sorted_merged_list = self.mergeTwoLists(list1, list2.next)
            list2.next = rem_sorted_merged_list
            return list2

                


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
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