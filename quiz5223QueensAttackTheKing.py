class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        '''
        从King点出发，从八个方向发散，找到第一个Queen
        定义queen为1，其他空位置为0,
        '''
        n = 8
        arr = [ [0 for j in range(n)] for i in range(n) ]
        #set queen to 1
        for x, y in queens:
            arr[x][y] = 1
        
        
        #king direction
        d = [[-1, 0], [-1, -1], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        ans = []
        for i in range(n):
            x, y = king
            while x >=0 and x < n and y>=0 and y < n:
                if arr[x][y] == 1:
                    ans.append([x, y])
                    break
                x, y = x+d[i][0], y+d[i][1]
        
        return ans