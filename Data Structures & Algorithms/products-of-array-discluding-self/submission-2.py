class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)

        for i, num in enumerate(nums):
            if i!=0:
                left[i] = nums[i-1] * left[i-1]
        
        right = [1] * len(nums)
        
        for j in range(len(nums)-1,-1,-1):
            if j!=len(nums)-1:
                right[j] = right[j+1] * nums[j+1]
        
        answer = [1] * len(left)

        for i in range(len(left)):
            answer[i] = left[i] * right[i]

        return answer
            


