class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        info = []

        def dfs(nums, ind, temp):
            if ind == len(nums):
                info.append(temp.copy())
                return 
            
            temp.append(nums[ind])
            ind+=1
            dfs(nums, ind, temp)
            temp.pop()
            dfs(nums, ind, temp)
            return 
        res = []
        dfs(nums, 0, res)
        print(info)
        return info

