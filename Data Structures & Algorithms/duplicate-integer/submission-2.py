class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         allVals = set()

         for num in nums:
            if num in allVals:
                return True 
            allVals.add(num)
        
         return False