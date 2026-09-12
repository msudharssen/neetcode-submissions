class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum = nums[0]
        currentSum = 0

        for num in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum+=num
            largestSum = max(largestSum, currentSum)
        return largestSum