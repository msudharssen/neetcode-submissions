class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        info = set()

        for num in nums:
            if num in info:
                return num 
            else:
                info.add(num)
        
        