class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''摩尔投票法修改版求众数(n//3), 要求O(n), O(1)'''
        
        n, x, y, cx, cy = len(nums), 0, 0, 0, 0
        
        for item in nums:
            if (cx == 0 or x == item) and y != item: # 对于每一个新的数字，优先跟x进行比较和运算，理论上排除x == y的情况
                x = item                             # 但是会出现整个数组一开始就是同一个数字组成的情况，在后面进行排查
                cx += 1
            elif cy == 0 or y == item:
                y = item
                cy += 1
            else:
                cx -= 1
                cy -= 1
        
        # 检验两个值是不是超过n//3
        res = []
        count = 0
        for num in nums:
            if x == num:
                count += 1
                if count > (n // 3):
                    res.append(x)
                    break
        count = 0
        for num in nums:
            if y == num:
                count += 1
                if count > (n // 3) and x != y: # 排除数组一开始就是同一个数字的情况
                    res.append(y) 
                    break
        return res