class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for index, element in enumerate(heights):
            start = index
            while stack and stack[-1][1]>element:
                prevIndex, prevHeight = stack.pop()
                maxArea = max(maxArea, abs(index-prevIndex)*prevHeight)
                start = prevIndex
            stack.append((start, element))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))
        return maxArea

