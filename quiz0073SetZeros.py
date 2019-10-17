class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #两个集合分别记录行或者列为0的标记
        rows = set()
        cols = set()
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for r in rows:
            for c in range(col):
                matrix[r][c] = 0
        for r in range(row):
            for c in cols:
                matrix[r][c] = 0
            