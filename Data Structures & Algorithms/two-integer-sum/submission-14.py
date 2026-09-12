class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        
        allNumbers = defaultdict()

        for k, num in enumerate(nums):
            difference = target - num
            if difference in allNumbers:
                return [allNumbers[difference],  k]
            allNumbers[num]=k

        return []

