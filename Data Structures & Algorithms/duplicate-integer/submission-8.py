class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        holdingDuplicateValues = set()
        for num in nums:
            if num in holdingDuplicateValues:
                return True
            holdingDuplicateValues.add(num)
        return False