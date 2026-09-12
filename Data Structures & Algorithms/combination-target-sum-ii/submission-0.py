class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(arr, ind, arr2, total):
            if total==target:
                res.append(arr.copy())
                return
            if total>target:
                return
            for i in range(ind, len(arr2)):
                if i > ind and arr2[i] == arr2[i-1]:  # <-- FIXED HERE
                    continue
                arr.append(arr2[i])
                dfs(arr, i+1, arr2, total+arr2[i])
                arr.pop()
        
        dfs([], 0, candidates, 0)
        return res
            