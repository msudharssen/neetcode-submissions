class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        def dfs(temp, arr, index, res, tar):
            if tar==target:
                info.append(temp.copy())
                return
            if index>=len(arr) or tar>target:
                return
            
            temp.append(arr[index])
            dfs(temp, arr, index, res, tar+arr[index])
            temp.pop()
            dfs(temp, arr, index+1, res, tar)

        
        info = []
        dfs([], nums, 0, info, 0)
        return info

            
            
