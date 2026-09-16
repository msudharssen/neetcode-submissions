class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = height[0]
        maxRight = height[-1]
        total = 0
        l = 0
        r = len(height)-1

        while l < r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            if maxLeft < maxRight:
                toAdd = min(maxLeft, maxRight)-height[l]
                total += toAdd if toAdd >= 0 else 0
                l+=1
            else:
                toAdd = min(maxLeft, maxRight)-height[r]
                total += toAdd if toAdd >=0 else 0
                r-=1
        return total
