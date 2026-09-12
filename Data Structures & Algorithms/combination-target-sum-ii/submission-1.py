class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       
        candidates.sort()
        res = []

        def traverse(trackArray, currTotal, index):
            if currTotal == target:
                res.append(trackArray.copy())
                return
            if currTotal>target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i]==candidates[i-1]:
                    continue
                trackArray.append(candidates[i])
                traverse(trackArray, currTotal+candidates[i], i+1)
                trackArray.pop()
        traverse([], 0, 0)
        return res

            

