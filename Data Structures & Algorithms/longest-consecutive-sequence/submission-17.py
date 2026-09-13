class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        allElements = set(nums)
        res = 0

        for num in nums:
            if(num-1) not in allElements:
                count = 1
                while num+count in allElements:
                    count+=1
                res = max(res, count)
        return res