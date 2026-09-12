class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [0]*((len(cost))+1)

        for i in range(len(res)-2,-1,-1):
            if i == len(res)-2:
                res[i]=cost[i]
            else:
                res[i]=min(res[i+1]+cost[i], cost[i]+res[i+2])
        print(res)
        return min(res[0], res[1])