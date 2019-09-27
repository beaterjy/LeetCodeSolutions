# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        '''英文题意中head是唯一的元素字符'''

        if not head:
            return 0

        # 方法一：使用标记
        # G = set(G)  # 集合中的in操作时间 << 列表中的in操作时间
            # 集合的in查找估计是哈希， 列表的in查找估计是顺序查找
        # p, count = head, 0
        # ok = False
        # while True:
        #     if not p:
        #         break
        #     if p.val in G:
        #         if not ok:
        #             count += 1
        #         # G.remove(p.val) # 唯一元素就不需要删除，不会重复
        #         ok = True
        #     else:
        #         ok = False
        #     p = p.next
        # return count

        # 方法二：两重循环
        G = set(G)
        p, count = head, 0
        while p:
            if p.val in G:
                count += 1
                while p.next:
                    p = p.next
                    if p.val not in G:
                        break
            p = p.next
        return count
