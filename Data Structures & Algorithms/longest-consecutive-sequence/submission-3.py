class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longestSeq = 0
        allVals = set(nums)

        for num in nums:
            curr = 1
            while num+curr in allVals:
                curr+=1
            longestSeq = max(longestSeq, curr)
        
        return longestSeq

        