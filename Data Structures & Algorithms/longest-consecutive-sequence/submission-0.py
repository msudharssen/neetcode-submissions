class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        seen = set(nums)

        
        for item in nums:
            if item - 1 not in seen:
                curr = 1
                
                while item + curr in seen:
                    curr+=1
              
                longest = max(longest, curr)
    
        return longest