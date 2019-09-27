class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''删除排序数组中的重复项'''
        if not nums:
            return 0
        
        index = 0
        for x in nums:
            if x not in nums[:index]:
                nums[index] = x
                index += 1
                
        return index
        