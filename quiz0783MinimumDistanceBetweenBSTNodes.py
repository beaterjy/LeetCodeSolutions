# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        '''
        首先树是二叉搜索树,
        可以通过中序遍历,得到排好序的数组,
        再求出最小差值
        '''
        arr = []
        def mid_travel(root):
            if root:
                mid_travel(root.left)
                arr.append(root.val)
                mid_travel(root.right)
        mid_travel(root)
        arr = [arr[i] - arr[i-1] for i in range(1, len(arr), 1)]
        return min(arr)
    