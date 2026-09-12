class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sortedArray = nums.sort()

        info = set()
        answer = []
        
        #[-1,0,1,2,-1,-4]

        for i in range(0,len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            else:
                l = i+1
                r = len(nums) -1
                while l < r:
                    totalSum = nums[i] + nums[l] + nums[r]
                    if totalSum == 0:
                        answer.append([nums[i], nums[l], nums[r]])
                        l+=1
                        while nums[l] == nums[l-1] and l < r:
                            l+=1
                    elif totalSum < 0:
                        l+=1
                    elif totalSum > 0:
                        r-=1
        return answer
                    



        