class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        secondArr = [0] * (len(nums) * 2)

        for i in range(len(nums)):
            secondArr[i] = nums[i]
            secondArr[i+len(nums)] = nums[i]
        
        return secondArr