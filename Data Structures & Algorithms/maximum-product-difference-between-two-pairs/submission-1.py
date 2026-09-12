class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maximum  = 0
        secondMax = 0
        minimum = float('inf')
        secondMinimum = float('inf')

        for num in nums:
            if num > maximum:
                maximum, secondMax = num, maximum
            elif num > secondMax:
                secondMax = num
            if num < minimum:
                minimum, secondMinimum = num, minimum
            elif num < secondMinimum:
                secondMinimum = num
        
        return (maximum * secondMax) - (minimum * secondMinimum) 