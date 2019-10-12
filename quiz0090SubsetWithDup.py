class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        回溯法
        最后过滤掉相同的元祖
        '''
        ans = []
        
        def backtrack(i, n, lst):
            if i < n:
                newLst = list(lst)
                backtrack(i+1, n, tuple(newLst))
                newLst.append(nums[i])
                backtrack(i+1, n, tuple(newLst))
            else:
                for tup in ans:
                    if tuple(tup) == lst:
                        break
                else:
                    ans.append(list(lst))
        
        
        nums.sort()
        backtrack(0, len(nums), tuple())
        return ans
        