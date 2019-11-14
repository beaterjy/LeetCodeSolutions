# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''删除倒数第n个节点，即删除第N=length-n+1个节点，
            对于N==1的情况：
            对于N!=1的情况
        '''
        if n == 0:
            return head
        
        length = 0
        p = head
        while True:
            if p == None:
                break
            length += 1
            p = p.next
        
        N = length - n + 1
        if N == 1:  #N == 1情况
            head = head.next
        else:   #N != 1情况
            p = head
            for i in range(1, N-1):
                p = p.next
            p.next = p.next.next
        return head
            