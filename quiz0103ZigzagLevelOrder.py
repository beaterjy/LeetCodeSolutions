# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        层次遍历
        last, nlast记录每一层最右边的位置
        对每一行进行正反顺序维护postive
        利用postive对这一行的值进行反转
        队列指针不需要反转
        '''
        if not root:
            return []
        
        ans = []
        queue = []
        p = root
        last, nlast = p, p
        postive = True
        queue.append(p)
        vals = []
        while True:
            if len(queue) == 0:
                break
            q = queue.pop(0)
            if q:
                vals.append(q.val)
            if q.left:
                nlast = q.left
                queue.append(q.left)
            if q.right:
                nlast = q.right
                queue.append(q.right)
                
            #到达每一行的末尾
            if q == last:
                if not postive:
                    vals.reverse()
                ans.append(vals)
                vals = []
                last = nlast
                postive = not postive
        return ans