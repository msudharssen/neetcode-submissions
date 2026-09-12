class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        if not heights:
            return area
        
        l = 0
        r = len(heights)-1

        while l < r:
            if heights[l] < heights[r]:
                area = max(area, (r-l)*heights[l])
                l+=1
            elif heights[r] <= heights[l]:
                area = max(area, (r-l)*heights[r])
                r-=1
        return area
