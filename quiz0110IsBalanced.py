# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            True
        
        
        #set val to height
        def to_height(root, ans):
            if not root:
                return 0
            A = to_height(root.left, ans)
            B = to_height(root.right, ans)
            root.val = max(A, B) + 1
            temp  = abs(A - B)
            if temp > 1:
                ans[0] = False
            return root.val
        
        ans = [True]
        to_height(root, ans)
        return ans[0]
                