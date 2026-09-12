class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        
        allNumbers = defaultdict()

        for i, num in enumerate(nums):
            allNumbers[num]=i
        
        for k, num in enumerate(nums):
            difference = target - num
            if difference in allNumbers and allNumbers[difference]!=k:
                return [k, allNumbers[difference]]

        return []

