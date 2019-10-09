class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        非递归实现
        定义第tri（i，j）为以（i，j）为顶的三角形的最小路径和
        自底向上进行维护这个最小路径三角形
        '''
        if not triangle:
            return 0
        for i in range(len(triangle)-2, -1, -1):
            for j in range(0, len(triangle[i])):
                A = triangle[i+1][j]
                B = triangle[i+1][j+1]
                triangle[i][j] = min(A, B) + triangle[i][j]
                
        return triangle[0][0]
                