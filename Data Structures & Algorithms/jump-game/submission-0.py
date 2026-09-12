class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currentIndex = 0
        for i in range(len(nums)):
            if i > currentIndex:
                return False
            currentIndex = max(currentIndex, i + nums[i])
            if currentIndex == len(nums)-1:
                return True
        
        return currentIndex >= len(nums) -1 