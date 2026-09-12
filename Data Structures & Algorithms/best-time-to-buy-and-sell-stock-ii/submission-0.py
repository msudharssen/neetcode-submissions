class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        profit = 0

        for num in prices:
            if num > start:
                profit += (num-start)
            start = num
        return profit