class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        输入为一个整数,将其转换成二进制,顺便记录其中1的个数
        '''
        ans = 0
        while True:
            if n % 2 == 1:
                ans += 1
            n = n // 2
            if not n:
                break
        return ans
                    