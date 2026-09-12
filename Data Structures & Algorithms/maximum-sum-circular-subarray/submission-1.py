class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        if not nums:
            return 0

        maxSum = nums[0]
        currMaxSum = 0

        minSum = nums[0]
        currMinSum = 0

        total = 0


        for num in nums:
            total += num

            currMaxSum += num
            currMaxSum = max(currMaxSum, num)
            maxSum = max(maxSum, currMaxSum)

            currMinSum+=num
            currMinSum = min(currMinSum, num)
            minSum = min(minSum, currMinSum)

        if total-minSum == 0:
            return maxSum
        
        return max(total-minSum, maxSum)