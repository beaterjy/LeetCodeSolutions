class Solution:
    def balancedStringSplit(self, s: str) -> int:
        '''
        顺序遍历，维护一个mark表示一个平衡字符串
        并统计数量
        '''
        if not s:
            return 0
        mark = 0
        count = 0
        for x in s:
            if x == 'L':
                mark += 1
            else:
                mark -= 1
            if mark == 0:
                count += 1
        
        return count