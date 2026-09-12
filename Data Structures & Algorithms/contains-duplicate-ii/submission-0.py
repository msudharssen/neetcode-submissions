class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        info = set()
        

        for r in range(len(nums)):
            if abs(r-l)>k:
                info.remove(nums[l])
                l+=1
            if nums[r] in info:
                return True
            info.add(nums[r])
            
        return False
                

                

