class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        res=0

        while l < r:
            if heights[l] <= heights[r]:
                currArea = heights[l]*(r-l)
                res = max(currArea, res)
                l+=1
            else:
                currArea = heights[r]*(r-l)
                res = max(currArea, res)
                r-=1
            print(res)
        return res


            

