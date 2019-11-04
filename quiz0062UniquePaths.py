class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        组合数C(m+n, n)
        '''
        def factorial(n):
            """阶乘"""
            if n == 0:
                return 1
            ans = 1
            for i in range(1, n+1):
                ans *= i
            return ans
        
        return int( factorial(m+n-2) / factorial(m-1) / factorial(n-1) )