class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        '''地下城游戏'''
        if not dungeon:
            return 1
        
        m, n = len(dungeon), len(dungeon[0])
        
        # 这种写法是错误的，列表是可变类型，*(m+1)是指复制m+1份，列表的浅复制只是复制引用，所有修改其中的一个内容，其他行会同时改变
        # hp = [[float('Inf')] * (n+1)] * (m+1) 
        
        hp = [[float('Inf') for i in range(n+1)] for i in range(m+1)]
        
        hp[m-1][n] , hp[m][n-1] = 1, 1
        
        for x in range(m-1, -1, -1):
            for y in range(n-1, -1, -1):
                hp[x][y] = max(1, min(hp[x][y+1], hp[x+1][y]) - dungeon[x][y])
                
        return hp[0][0]