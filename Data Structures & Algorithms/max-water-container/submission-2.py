class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) -1
        maxArea = 0

        while l < r:
            temp = min(heights[l], heights[r])
            currentArea = (temp * abs(l-r))
            maxArea = max(maxArea, currentArea)
            if temp==heights[l]:
                l+=1
            elif temp==heights[r]:
                r-=1
        
        return maxArea
        