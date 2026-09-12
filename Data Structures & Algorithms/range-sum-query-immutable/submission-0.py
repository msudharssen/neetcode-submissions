class NumArray:

    def __init__(self, nums: List[int]):
        self.hashMap = {}
        self.currSum = 0
        self.vals = nums.copy()

        for i, num in enumerate(nums):
            self.currSum += num
            self.hashMap[i]=self.currSum

    def sumRange(self, left: int, right: int) -> int:
        if self.vals and left >=0 and right<len(self.vals):
            return self.hashMap[right]-self.hashMap[left]+self.vals[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)