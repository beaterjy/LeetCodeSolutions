# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #对于链表，分成前后两部分
        #对于后一半部分，先利用头插法进行逆序
        #最后再利用双指针进行合并
        #pring the link
        def print_link(head):
            head = head.next
            if not head:
                return 
            while head:
                print(head.val, end=',')
                head = head.next
        
        if not head:
            return head
        
        length = 0
        h1 = head
        while h1:
            length += 1
            h1 = h1.next
        
        h2 = head
        for i in range(length // 2):
            h2 = h2.next
        # new a empty head2
        tmp  = ListNode(0)
        tmp.next = h2
        h2 = tmp
        # reverse the behind link
        # new another link2
        link2 = ListNode(0)
        mark_link2 = link2 
        while h2.next:
            p = h2.next
            h2.next = p.next
            # take the p to link2
            p.next = link2.next
            link2.next = p
        # print the link2
        # print_link(mark_link2)
        
        # two order link
        h2 = mark_link2
        
        # new a ans link
        h3 = ListNode(0)
        p3 = h3
        h1 = ListNode(0)
        h1.next = head
        p, q = h1, h2
        while h1.next and h2.next:
            if h1.next:
                p = h1.next
                h1.next = p.next
            p3.next = p
            p3 = p3.next
            if h2.next:
                q = h2.next
                h2.next = q.next
            p3.next = q
            p3 = p3.next
        p3.next = None
        return h3.next