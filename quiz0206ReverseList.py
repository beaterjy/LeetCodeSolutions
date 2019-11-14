# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 头插法倒序
        if not head:
            return head
        
        nhead = ListNode(0)
        while head:
            p = head
            head = head.next
            p.next = nhead.next
            nhead.next = p
        return nhead.next