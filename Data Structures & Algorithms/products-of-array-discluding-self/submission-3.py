class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)

        for i, num in enumerate(nums):
            if i!=0:
                left[i] = nums[i-1] * left[i-1]
        
        temp = 1
        for j in range(len(nums)-1,-1,-1):
            if j!=len(nums)-1:
                temp = temp * nums[j+1]
                left[j] = left[j] * temp


        return left
            


