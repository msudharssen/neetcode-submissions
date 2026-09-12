class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
         res = []
         summ = 0
         nums.sort()


         def dfs(arr, ind, arr2, total):
            if total==target:
                res.append(arr.copy())
                return
            if total >target:
                return

            
            for i in range(ind, len(arr2)):
                arr.append(arr2[i])
                dfs(arr, i, arr2, total+arr2[i])
                arr.pop()
        
         dfs([], 0, nums, summ)
         return res
