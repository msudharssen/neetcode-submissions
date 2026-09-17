class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for num in prices:
            buy = min(buy, num)
            if num > buy:
                profit = max(profit, num-buy)
        return profit
