class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        DP
        定义dp[r][i]为前i项的最大和
        填充一个二维数组
        * 其中要初始化第一个出现且当前%3分别为0，1，2的值
        * 最大值为max(A, B, dp[r][i])
        """
        if not nums:
            return 0
        
        n = len(nums)
        # define 2-dim dp arr(3, n)
        dp = [ [0 for i in range(n)] for r in range(3)]
        
        # fill the first appear
        for i in range(n):
            ithr = nums[i] % 3
            dp[ithr][i] = nums[i]
        
        for i in range(1, n):
            for r in range(3):
                ithr = nums[i]%3
                if dp[(r-ithr)%3][i-1] > 0:
                    A = dp[(r-ithr)%3][i-1] + nums[i]
                else:
                    A = 0
                B = dp[r][i-1]
                dp[r][i] = max(A, B, dp[r][i])
        # print(dp)
        return dp[0][n-1]