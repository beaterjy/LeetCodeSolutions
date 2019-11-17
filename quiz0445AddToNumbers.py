# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 读取出两个整数，相加后再存储到一个新的链表中
        if not l1 or not l2:
            if not l1 and not l2:
                return None
            elif not l1:
                return l2
            else:
                return l1

        num1, num2 = 0, 0
        # link1 to num1
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        # link2 to num2
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        # add num1 and num2
        num3 = num1 + num3
        # build the link3
        link3 = ListNode(0)
        l3 = link3
        # num3 == 0
        if num3 == 0:
            return link3
        # head insert to reverse
        while num3:
            tmp = ListNode(num3 % 10)
            tmp.next = l3.next
            l3.next = tmp
            num3 = num3 // 10
        return link3.next
            