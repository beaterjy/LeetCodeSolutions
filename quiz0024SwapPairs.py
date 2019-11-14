# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        对于接下来的两个节点node1,node2，
        将node2插入到node1之前
        '''
        #新建头部节点
        h = ListNode(0)
        h.next = head
        head = h
        p = head
        
        #接下来的两个节点 
        while True:
            node1 = p.next
            if not node1: #到达末端
                break
            node2 = p.next.next
            if not node2: #到达末端 
                break
            #将node2插入到node1之前
            node1.next = node2.next
            node2.next = node1
            p.next = node2
            #递增2位
            p = p.next.next
        head = head.next
        return head
            