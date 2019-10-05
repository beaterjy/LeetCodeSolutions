class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        定义m[i]为到达i时最大的爬楼梯方法
        '''
        m = [0] * (n+1)
        def f(n):
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 2
            if m[n] != 0:
                return m[n]
            m[n] = f(n-1) + f(n-2)
            return m[n]
        
        return f(n)