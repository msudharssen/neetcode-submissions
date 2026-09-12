class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        total = 0
        right = len(heights)-1
        while left < right:
            current = (min(heights[right], heights[left]) * (right-left))
            total = max(total, current)
            if heights[right] > heights[left]:
                left+=1
            else:
                right-=1
        return total


