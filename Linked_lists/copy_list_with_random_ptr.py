# O(n) time and O(1) space



class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #could simply do x = copy.deepcopy(head) and will get
        # O(n) time and O(n) space but this isn't what they are asking us
        
        
        if not head:
            return None

        # A -> B -> C -> NULL to A -> A' -> B -> B' -> C -> C'-> NULL
        # such that A.next = A' and A'.val = A.val. We don't do anything with rand ptr right now
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        #Now fix random ptr
        # A'.random = A.random.next and so on and so forth
        # because if A.random is C, A.random.next will be C' which is what we want

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
       
        
        # Now removing A, B, C such that we only have A' -> B' -> C' -> NULL

        
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next # restore original list
            copy.next = copy.next.next if copy.next else None
            curr = curr.next

        return copy_head


    




        