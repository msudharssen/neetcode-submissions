class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for r in range(len(prices)):
            if prices[r] < buy:
                buy = prices[r]
            else:
                profit = max(profit, prices[r]-buy)
        return profit