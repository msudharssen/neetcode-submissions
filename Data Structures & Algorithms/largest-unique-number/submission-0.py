class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        info = Counter(nums)
        maxNumber = -1
        for k, v in info.items():
            if v == 1:
                maxNumber = max(maxNumber, k) 
        return maxNumber
