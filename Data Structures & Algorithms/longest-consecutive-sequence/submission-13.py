class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        info = set(nums)

        for num in nums:
            if num-1 not in info:
                temp = 1
                while num + temp in info:
                    temp+=1
                res = max(res, temp)
        return res
