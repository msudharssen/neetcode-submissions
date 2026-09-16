class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = height[0]
        maxRight = height[-1]
        total = 0
        l = 0
        r = len(height)-1

        while l < r:
            if maxLeft < maxRight:
                l+=1
                maxLeft = max(maxLeft, height[l])
                toAdd = min(maxLeft, maxRight)-height[l]
                total += toAdd if toAdd >= 0 else 0
            else:
                r-=1
                maxRight = max(maxRight, height[r])
                toAdd = min(maxLeft, maxRight)-height[r]
                total += toAdd if toAdd >=0 else 0
        return total
