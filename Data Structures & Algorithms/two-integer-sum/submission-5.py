class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        allVals = {}
        answer = []

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in allVals:
                answer.append(allVals[diff])
                answer.append(i)
                return answer
            else:
                allVals[nums[i]] = i

        return answer