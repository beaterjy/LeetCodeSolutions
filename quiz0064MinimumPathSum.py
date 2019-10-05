class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        非递归实现二维数组最小路径和
        '''
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        
        #the 0th row
        for y in range(1, col):
            grid[0][y] = grid[0][y-1] + grid[0][y]
        
        #the 0th col
        for x in range(1, row):
            grid[x][0] = grid[x-1][0] + grid[x][0]
        
        for x in range(1, row):
            for y in range(1, col):
                A = grid[x-1][y]
                B = grid[x][y-1]
                grid[x][y] = min(A, B) + grid[x][y]
        
        return grid[row-1][col-1]
    
    