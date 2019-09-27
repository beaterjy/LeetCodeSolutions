class Solution:
    def romanToInt(self, s: str) -> int:
        '''罗马数字转整数'''
        romans = {
            'I':1
            ,'V':5
            ,'X':10
            ,'L':50
            ,'C':100
            ,'D':500
            ,'M':1000
        }
        
        nums = [romans[x] for x in s]
      
        ans = 0
        for i, x in enumerate(nums):
            if i > 0 and nums[i] > nums[i-1]:
                nums[i] -= nums[i-1]
                nums[i-1] = 0
        for x in nums:
            ans += x
        return ans
        
        