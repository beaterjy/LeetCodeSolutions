# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''用一个字典保存val跟次数，O(n)
            再用集合保存只出现一次的val值
            用另一个链表存储结果O(n)
        '''
        if not head:
            return head
        
        d = dict()
        p = head
        while p:
            if p.val in d:
                d[p.val] += 1
            else:
                d[p.val] = 1
            p = p.next
        
        #遍历链表，创建一个只有一次val的集合
        s = set()
        for k, v in d.items():
            if v == 1:
                s.add(k)
        #如果集合s为空
        if not s:
            return None
        
        #遍历链表，创建新链表
        head2 = []
        q = head2
        p = head
        while p:
            if p.val in s:
                if not head2:
                    head2 = p
                    q = p
                else:
                    q.next = p
                    q = q.next
            p = p.next
        #结尾部分为None
        q.next = None
        return head2