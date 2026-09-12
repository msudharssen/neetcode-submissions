class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right=[1]*len(nums)
        output=[1]*len(nums)

        for i in range(len(nums)):
            if i==0:
                left[i]=1
            else:
                left[i]=left[i-1]*nums[i-1]
       
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                right[i]=1
            else:
                right[i]=nums[i+1]*right[i+1]
        
        for i in range(len(left)):
            output[i]=left[i]*right[i]
        return output
        