class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allNumbers = set(nums)
        total = 0

        for num in nums:
            curr = 1
            while num + curr in allNumbers:
                curr+=1
            total = max(total, curr)
        return total
            