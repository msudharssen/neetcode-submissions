class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        info = defaultdict()

        for i in range(len(nums)):
            info[nums[i]] = i


        for i in range(len(nums)):
            if target - nums[i] in info and info[target-nums[i]] != i:
                return list((i, info[target-nums[i]]))
        
        return []