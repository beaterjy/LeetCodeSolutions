# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 输出二叉树
    def printTree(self, root: TreeNode) -> List[List[str]]:
        height = self.heightOfTree(root)
        width = 2 ** height - 1
        
        arr = self.initArr(height, width)
        
        self.update_arr(root, 0, width, 0, arr)
        
        return arr
    
    
    def heightOfTree(self, T):
        if T == None:
            return 0
        return max(self.heightOfTree(T.left), self.heightOfTree(T.right)) + 1
    
    def initArr(self, height, width):
        return [[''] * width for i in range(height)]
    
    def update_arr(self, node, left, right, row, arr):
        if not node:
            return 
        mid = (left + right) // 2
        arr[row][mid] = str(node.val)
        self.update_arr(node.left, left, mid-1, row+1, arr)
        self.update_arr(node.right, mid+1, right, row+1, arr)