class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        l = 0

        for r in range(0,len(nums)-k+1):
            maxValue = max(nums[r:r+k])
            output.append(maxValue)
        
        return output


        