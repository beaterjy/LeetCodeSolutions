class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        # 全排列， 最后排列出来的重复的不加进res中，时间复杂度大
        # 通过剪枝可以减少时间复杂度
        def df(nums, ls, res):
            if not nums:
                # if ls not in res:
                #     res.append(ls)
                res.append(ls) # 剪枝过后可以省去判断
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]: # （剪枝）如果当前要分配的数字跟前一个数字相同，说明情况跟前一个数字一样，已经排列好了一种情况了
                    continue
                
                # ls2 = ls[:]
                # ls2.append(nums[i])
                # nums2 = nums[:]
                # del nums2[i]
                # df(nums2, ls2, res)
                
                df(nums[:i]+nums[i+1:], ls[:]+[nums[i]], res) # 优化写法
                
        '''全排列，有重复元素，排列后只保留一种重复情况'''
        nums.sort()
        res = []
        
        if not nums:
            return res
        
        df(nums, [], res)
        
        return res 

        
    
    
    
        