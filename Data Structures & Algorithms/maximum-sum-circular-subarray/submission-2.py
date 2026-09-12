class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currMaxSum = 0
        total = 0
        minSum = nums[0]
        currMinSum = 0

        for num in nums:
            total+=num
            currMaxSum = max(currMaxSum+num, num)
            maxSum = max(currMaxSum, maxSum)
            currMinSum = min(currMinSum+num, num)
            minSum = min(currMinSum, minSum)
        
        if total - minSum == 0:
            return maxSum
        
        return max(total-minSum, maxSum)
        