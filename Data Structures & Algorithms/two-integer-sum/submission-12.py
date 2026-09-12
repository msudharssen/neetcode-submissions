class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        indOfNumbers = defaultdict()


        for ind, num in enumerate(nums):
            difference = target - num
            if difference in indOfNumbers and ind!=indOfNumbers[difference]:
                res.append(indOfNumbers[difference])
                res.append(ind)
                return res
            indOfNumbers[num] = ind

        return res

            