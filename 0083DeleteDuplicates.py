# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        用一个集合存储已经出现了一次的元素的值
        对于每一个结点，判断是否已经出现了
        '''
        if not head:
            return head
        
        s = set()
        res, start = head, head
        s.add(res.val)
        p = res.next
        while p:
            if p.val not in s:
                s.add(p.val)
                res.next = p
                res = res.next
            p = p.next
        res.next = None
        return start