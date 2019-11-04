class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        回溯法
        '''
        ans = []
        
        def backtrack(i, n, lst):
            if i < n:
                newLst = list(lst)
                backtrack(i+1, n, tuple(newLst))
                newLst.append(nums[i])
                backtrack(i+1, n, tuple(newLst))
            else:
                ans.append(list(lst))
        
        
        backtrack(0, len(nums), tuple())
        return ans
            