class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                first = nums[i]
                second = i+1
                last = len(nums)-1

                while second < last:
                    if nums[second]+nums[last]+first > 0:
                        last-=1
                    elif nums[second]+first+nums[last]<0:
                        second+=1
                    else:
                        res.append([first, nums[second], nums[last]])
                        second+=1
                        while nums[second]==nums[second-1] and second < last:
                            second+=1
        return res