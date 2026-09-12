class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftArray = [1] * len(nums)
        rightArray = [1] * len(nums)
        answer = [0] * len(nums)
        ind = 1
        for i in range(0, len(nums)):
            if ind == len(nums): 
                break
            else:
                leftArray[ind] = nums[i]*leftArray[ind-1]
                ind+=1
        
       
        f = len(nums)-2
        for i in range(len(nums)-1, -1, -1):
            if f<0: 
                break
            else:
                rightArray[f] = nums[i]*rightArray[f+1]
                f-=1
        
        for i in range(len(nums)):
            answer[i] = leftArray[i] * rightArray[i]

        return answer
        