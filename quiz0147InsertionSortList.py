# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 首先创建头节点
        # 实现插入排序
        if not head:
            return head

        nhead = ListNode(0)
        nhead.next = head
        head = nhead

        # insert sort 
        # find min num 's front node
        while True:
            p = head
            if not p.next:
                break
            else:
                min_num = p.next.val
                min_fp = p
            while p.next:
                if p.next.val < min_num:
                    min_fp = p
                    min_num = p.next.val
                p = p.next
            # insert
            tmp = min_fp.next
            min_fp.next = min_fp.next.next
            tmp.next = head.next
            head.next = tmp
            head = head.next
        return nhead.next