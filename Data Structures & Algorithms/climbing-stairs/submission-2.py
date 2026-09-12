class Solution:
    def climbStairs(self, n: int) -> int:
        infoArray = [0] * 3
        infoArray[0]=1
        infoArray[1]=2
        infoArray[2]=3

        if n<3:
            return infoArray[n-1]

        h = [0] * (n)
        h[0] = 1
        h[1] = 2
        h[2] = 3
        for r in range(3, n):
            h[r] = h[r-1]+h[r-2]
        return h[-1]



