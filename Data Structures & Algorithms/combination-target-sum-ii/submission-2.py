class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        #[10,1,2,7,6,1,5]
        #[1,1,2,5,6,7,10]

        def traverse(index, currSum, temp):
            if currSum==target:
                res.append(temp.copy())
                return
            if currSum>target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i]==candidates[i-1]:
                    continue
                toAdd = candidates[i]+currSum
                temp.append(candidates[i])
                traverse(i+1, toAdd, temp)
                temp.pop()
        traverse(0,0,[])
        return res