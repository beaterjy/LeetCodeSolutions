class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''求众数'''
#         # 方法一O(logn): 排序，再选择中间的数
#         if not nums:
#             return None

#         nums.sort()
#         return nums[(0 + len(nums) // 2)]

#         '''----------------------------------------------------------------------'''

#         # 该题目的众数一定大于 n//2, 且数组非空
#         # 方法二O(n): 用字典统计每一个出现数字的个数，如果有数字大于 n//2, 则返回
#         d = {}
#         n = len(nums)
#         for item in nums:
#             d.setdefault(item, 0)
#             d[item] += 1
#             if d[item] > (n // 2):
#                 return item
#         return 0

        '''-------------------------------------------------------------------------'''

        # 方法三O(n)O(1): 摩尔投票法
        x, cx = 0, 0
        for num in nums:
            if cx == 0 or x == num:
                x = num
                cx += 1
            else:
                cx -= 1

        # 检验所得到的值是否大于n // 2
        count, n = 0, len(nums)
        for num in nums:
            if x == num:
                count += 1
                if count > (n // 2):
                    return x
        return -1
