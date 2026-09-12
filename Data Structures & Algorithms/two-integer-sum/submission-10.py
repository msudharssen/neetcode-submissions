class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        indOfNumbers = defaultdict()

        for i, n, in enumerate(nums):
            indOfNumbers[n]=i

        for ind, num in enumerate(nums):
            difference = target - num
            if difference in indOfNumbers and ind!=indOfNumbers[difference]:
                res.append(ind)
                res.append(indOfNumbers[difference])
                return res
        return res
        
            