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
        # Dummy node to simplify head handling
        dummy = ListNode(-1)
        current = dummy #aliases pointing to an address in memory

        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                # We are modifying the next attribute of the object that both current and dummy point to
                list1 = list1.next
            else:
                current.next = list2
                # We are modifying the next attribute of the object that both current and dummy point to
                list2 = list2.next
            current = current.next
            # Now current stops pointing to the dummy node and starts pointing to the next node (list1 or list2)

        # Attach remaining nodes
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # Return head of merged list
        return dummy.next