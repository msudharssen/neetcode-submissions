class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxNumber = nums[0]
        runningTotal = 0

        for num in nums:
            runningTotal = max(runningTotal + num, num)
            maxNumber = max(runningTotal, maxNumber)
        return maxNumber
