class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        info = set()
        l = 0

        for r in range(len(nums)):
            if r-l+1 >k+1:
                info.remove(nums[l])
                l+=1
            if nums[r] in info:
                return True
            info.add(nums[r])

        return False