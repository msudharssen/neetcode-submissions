class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            else:
                res = max(res, price-buy)
        return res
