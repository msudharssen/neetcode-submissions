class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        res = float('inf')

        for r in range(len(nums)):
            if r-l+1 == k:
                res = min(res, abs(nums[r]-nums[l]))
                l+=1
        return res
        
