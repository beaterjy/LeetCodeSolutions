# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        '''二叉树的坡度'''
        self.s = 0
        
        def sumtree(root):
            if not root:
                return 0
                
            left = sumtree(root.left)
            right = sumtree(root.right)
            self.s += abs(left - right)
            return root.val + left + right
        
        sumtree(root)
        return self.s
    
    
        