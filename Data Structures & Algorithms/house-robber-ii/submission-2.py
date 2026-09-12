class Solution:
    def rob(self, nums: List[int]) -> int:
    
        return max(self.normalRobber(nums[1:]), self.normalRobber(nums[:-1]), nums[0])


    def normalRobber(self, temp):
        rob1, rob2 = 0, 0
        for i in range(len(temp)):
            curRob = max(rob1+temp[i], rob2)
            rob1 = rob2
            rob2 = curRob
        return rob2
        