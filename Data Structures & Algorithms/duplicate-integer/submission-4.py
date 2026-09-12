class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        info = set()

        for i in range(len(nums)):
            if nums[i] in info:
                return True
            else:
                info.add(nums[i])
        return False