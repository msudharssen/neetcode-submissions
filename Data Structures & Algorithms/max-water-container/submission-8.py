class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0

        while l < r:
            if heights[l]>=heights[r]:
                currArea = abs(l-r) * min(heights[l], heights[r])
                r-=1
            elif heights[l]<heights[r]:
                currArea = abs(l-r) * min(heights[l], heights[r])
                l+=1
            res = max(res, currArea)
        return res