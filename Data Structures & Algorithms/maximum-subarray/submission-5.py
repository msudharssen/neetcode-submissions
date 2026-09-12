class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            currSum = max(num+currSum, num)
            maxSum = max(currSum, maxSum)
        return maxSum