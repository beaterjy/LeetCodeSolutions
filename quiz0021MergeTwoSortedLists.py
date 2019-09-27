# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''合并两个链表'''

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        ll = ListNode(0)
        p = ll
        while l1 and l2:
            if l1.val <= l2.val:
                ll.next = l1
                l1 = l1.next
            else:
                ll.next = l2
                l2 = l2.next
            ll = ll.next
        if l1:
            ll.next = l1
        if l2:
            ll.next = l2

        return p.next
