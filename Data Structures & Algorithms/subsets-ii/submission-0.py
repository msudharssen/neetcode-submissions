class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(arr, ind, arr2, ref):
            if ind >= len(arr2):
                ref.append(arr.copy())
                return
            
            arr.append(arr2[ind])
            dfs(arr,ind+1, arr2,ref)
            arr.pop()
            while ind+1 < len(arr2) and arr2[ind]==arr2[ind+1]:
                ind+=1
            dfs(arr,ind+1,arr2,ref)
            return
        dfs([], 0, nums, res)
        return res