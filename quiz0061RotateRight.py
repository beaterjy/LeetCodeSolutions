# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''向右移动k个位置，即头节点为N=lengeth-k+1,
            可以先制造循环链表
            
        '''
        if k == 0:
            return head
        if not head:
            return head
        
        #循环链表
        length = 1
        p = head
        while p.next != None:
            length += 1
            p = p.next
        p.next = head
        
        #k重定向
        k = k % length
        
        #找到N-1， N位置，N-1位置的next为None
        N = length - k + 1
        p = head
        for i in range(1, N-1):
            p = p.next
        head = p.next
        p.next = None
        return head