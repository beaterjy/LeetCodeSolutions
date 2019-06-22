class Solution:
      # 全排列
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        else:
            self.fun(arr=[], others=nums, res=res)
            return res
        
    
    
    def fun(self, arr, others, res):
        if others == []:
            res.append(arr)
        for item in others:
            arr2 = arr[:]
            arr2.append(item)
            others2 = others[:]
            others2.remove(item)
            self.fun(arr2, others2, res)
        
