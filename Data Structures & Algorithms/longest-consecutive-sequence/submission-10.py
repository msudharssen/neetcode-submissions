class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        - Input is valid?
        - duplicates?
        [2,20,4,10,3,4,5]
        2,3,4,5
        10
        20
        """

        toReturn = 0
        setOfVals = set(nums)

        for num in nums:
            current = 1
            if num-1 not in setOfVals:
                while num+current in setOfVals:
                    current+=1
                toReturn = max(current, toReturn)
        return toReturn

