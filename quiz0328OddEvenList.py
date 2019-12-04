# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        split odd link and even link
        combine both of links
        """
        if not head:
            return head

        # new even link
        evenLink = ListNode(0)
        evenP = evenLink
        # new odd link
        oddLink = ListNode(0)
        oddP = oddLink
        # isOdd label
        isOdd = True
        p = head
        while p:
            if isOdd:
                oddP.next = p
                oddP = oddP.next
            else:
                evenP.next = p
                evenP = evenP.next
            isOdd = not isOdd
            p = p.next
        # combine two links
        oddP.next = None
        evenP.next = None
        evenLink = evenLink.next
        oddP.next = evenLink
        oddLink = oddLink.next
        
        return oddLink