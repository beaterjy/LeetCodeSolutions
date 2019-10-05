class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #非递归实现
        #定义opt为前项的最佳解决方案
        opt = [0] * len(nums) 
        opt[0] = nums[0]
        
        for i in range(1, len(opt)):
            A = opt[i-1] + nums[i]
            B = nums[i]
            opt[i] = max(A, B)
            
        return max(opt)
        