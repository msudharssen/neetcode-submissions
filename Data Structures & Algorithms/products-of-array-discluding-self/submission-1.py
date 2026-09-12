class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(len(nums)):
            if i==0:
                left[i] = 1
            else:
                left[i] = nums[i-1] * left[i-1]
        
        print(left)
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                right[i] = 1
            else:
                right[i] = right[i+1] * nums[i+1]
        print(right)

        for j in range(len(res)):
            res[j] = left[j] * right[j]

        print(res)
        return res 

        

        
