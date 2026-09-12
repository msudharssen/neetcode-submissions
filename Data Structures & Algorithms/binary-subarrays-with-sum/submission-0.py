class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def traverse(x):
            if x < 0: return 0
            res = 0
            l = 0
            currSum = 0
            for r in range(len(nums)):
                currSum += nums[r]
                while currSum > x:
                    currSum-=nums[l]
                    l+=1
                res += (r-l+1)
            return res
        return traverse(goal) - traverse(goal-1)
