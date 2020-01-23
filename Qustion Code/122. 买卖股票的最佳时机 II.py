# method_1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(1,n):
            t = prices[i] - prices[i-1]
            if t > 0:
                profit += t
        
        return profit