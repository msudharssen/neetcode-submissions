class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        ans = []
        nums.sort()
        print(nums)

        currNum = nums[0]
        count = 1

        for i in range(1,len(nums)):
            if currNum!=nums[i]:
                if count > len(nums)//3:
                    ans.append(currNum)
                currNum = nums[i]
                count = 1
            else:
                count+=1
        
        if count > len(nums)//3:
            ans.append(currNum)

        return ans