class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [float('inf')]* (amount+1)
        res[0] = 0

        for i in range(len(res)):
            for coin in coins:
                dif = i - coin
                if dif >= 0:
                    res[i] = min(res[i],res[i-coin] + 1)
        return res[amount] if res[amount]!=float('inf') else -1

