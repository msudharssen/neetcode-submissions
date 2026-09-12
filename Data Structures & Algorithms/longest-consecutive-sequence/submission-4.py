class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        allVals = set(nums)
        res = 0

        for num in nums:
            curr = 1
            while num+curr in allVals:
                curr+=1
            res = max(res, curr)
       
        return res