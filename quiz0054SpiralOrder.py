class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''螺旋矩形'''
        if not matrix:
            return []
        
        res = []
        
        rows_n = len(matrix)
        cols_n = len(matrix[0])
        
        # 前进方向
        di, dj = 0, 1
        # 起点坐标
        i, j = 0, 0
        
        for t in range(rows_n * cols_n):
            res.append(matrix[i][j])
            matrix[i][j] = ''
            if matrix[(i+di)%rows_n][(j+dj)%cols_n] == '': 
                di, dj = dj, -di # 改变方向
            i, j = i+di, j+dj
        return res