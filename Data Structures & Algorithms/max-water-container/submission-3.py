class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0 

        l = 0
        r = len(heights) - 1

        while l < r:
            temp = min(heights[l], heights[r])
            maxArea = max(maxArea, temp * (r-l))
            if temp == heights[l]:
                l+=1
            else:
                r-=1
        
        return maxArea
            
