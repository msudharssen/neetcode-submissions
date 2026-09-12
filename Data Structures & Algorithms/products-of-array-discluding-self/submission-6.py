class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        left = [1]*len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]

        right = [1]*len(nums)
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        
        res = [1]*len(nums)
        for k in range(len(nums)):
            res[k] = left[k]*right[k]
        print(res)
        return res
            
        
