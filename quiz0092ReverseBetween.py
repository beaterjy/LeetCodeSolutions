# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        对m到n之间实现反转，使用头插法
        '''
        if not head:
            return head
        if m == n:
            return head
        
        #新建头节点
        p = ListNode(x=0)
        p.next = head
        head = p
        
        #head2, tail2设为子链表的头和尾部
        length = 0
        p = head.next
        while True:
            if not p:
                break
            length += 1
            if length == m: #子链表首部
                head2 = p
            if length == n: #子链表尾部
                tail2 = p
            p = p.next
            
        #找到要头插法插入的位置
        p = head  
        while p.next != head2:
            p = p.next
        #子链表外相连
        p.next = tail2.next
        #子链表右边指针
        final_lst = tail2.next
        
        #实现头插法
        while True:
            q = head2
            head2 = head2.next
            #头插入
            q.next = p.next
            p.next = q
            if head2 == final_lst:
                break
            
        #修正头指针
        head = head.next
        return head