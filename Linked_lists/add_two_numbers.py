# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = l1
        prev = None

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            if l1:
                l1.val = total % 10
                prev = l1
                l1 = l1.next
            else:
                prev.next = ListNode(total % 10)
                prev = prev.next

            if l2:
                l2 = l2.next

        if carry:
            prev.next = ListNode(carry)

        return head

            
                
'''Important note: While the space complexity is O(1) in terms of auxiliary space, the algorithm does modify the input l1 destructively. If you count the output space (which is sometimes included in space complexity analysis), it would be O(max(m, n)) since the result list has that many nodes. However, by the standard definition that excludes output space, this is O(1).'''

        