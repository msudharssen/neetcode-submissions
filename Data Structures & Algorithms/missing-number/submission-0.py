class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        info = set(nums)
        temp = len(nums)

        while temp > 0:
            if temp in info:
                temp-=1
            else:
                break
        
        return temp