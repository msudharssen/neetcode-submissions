class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<4:
            return 0
        
        return (nums[-1]*nums[-2]) - (nums[0]*nums[1])