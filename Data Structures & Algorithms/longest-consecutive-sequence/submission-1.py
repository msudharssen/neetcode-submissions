class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longestSeq = 0
        setOfNums = set(nums)

        for numb in nums:
            curr = 1

            while numb + curr in setOfNums:
                curr+=1
            
            longestSeq = max(curr, longestSeq)
        
        return longestSeq