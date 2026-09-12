class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        lowest = prices[0]

        for num in prices:
            if num < lowest:
                lowest = num
            else:
                profit = max(profit, num - lowest)
        
        return profit