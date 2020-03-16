# method_2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            else:
                max_profit = max(prices[i]-prices[buy],max_profit)
        return max_profit