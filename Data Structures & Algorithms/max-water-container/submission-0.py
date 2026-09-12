class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        mostWater = 0

        while l < r:
            temp = min(heights[l], heights[r])
            mostWater = max(mostWater, temp * abs(l -r))

            if temp == heights[l]:
                l+=1
            elif temp == heights[r]:
                r-=1
        
        return mostWater

        