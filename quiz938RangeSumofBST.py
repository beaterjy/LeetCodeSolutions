# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        '''
        二叉搜索树
        遍历二叉树,如果值再L和R之间,则返回值,否则返回0
        '''
        if not root:
            return 0
        temp = 0
        if root.val >= L and root.val <= R:
            temp = root.val
        return temp + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
    
    