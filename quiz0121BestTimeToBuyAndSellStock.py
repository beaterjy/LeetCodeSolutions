class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        时间复杂度：O(n)
        一次遍历数组，维护一个最小值minprice, 和一个最大利润maxprofit
        '''
        minprice, maxprofit = float('inf'), 0
        for x in prices:
            if x < minprice:
                minprice = x
            else:
                if x - minprice > maxprofit:
                    maxprofit = x - minprice
        return maxprofit