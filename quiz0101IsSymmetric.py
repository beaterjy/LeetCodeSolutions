# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        两个孩子树同时进行镜像比较
        '''
        def isMirror(left, right):
            if not left and not right:
                return True
            elif left and right:
                return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
            else:
                return False
        
        if not root:
            return True
        else:
            return isMirror(root.left, root.right)