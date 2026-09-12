class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         info = set()

         for num in nums:
            if num in info:
                return True
            else:
                info.add(num)
         return False