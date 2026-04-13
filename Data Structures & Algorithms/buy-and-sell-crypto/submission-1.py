class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_val, profit = float('inf'), 0
        for i in range(len(prices)):
            currProfit = prices[i]- buy_val
            if currProfit>profit:#if selling at current selling price
                profit=currProfit #update profit
            if buy_val>prices[i]:# if buying at current price
                buy_val=prices[i]
        return profit