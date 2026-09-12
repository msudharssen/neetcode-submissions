class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            currSum += num
            currSum = max(currSum, num)
            maxSum = max(maxSum, currSum)
        return maxSum