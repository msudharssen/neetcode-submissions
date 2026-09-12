class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        info = set(nums)

        for num in nums:
            curr = 1
            if num - 1 not in info:
                while num+curr in info:
                    curr+=1
                ans=max(curr, ans)
        return ans
