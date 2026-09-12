class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        total = nums[0]
        curr = 0

        for numb in nums:
            if curr < 0:
                curr = 0
            curr+=numb
            total = max(total, curr)
        
        return total


        