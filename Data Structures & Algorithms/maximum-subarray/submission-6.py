class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        currSum = 0

        for i in range(len(nums)):
            currSum = currSum + nums[i]
            currSum = max(currSum, nums[i])
            res = max(currSum, res)
        return res