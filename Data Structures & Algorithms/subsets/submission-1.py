class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def traverse(currentEl, index, ans):
            if index==len(nums):
                copy = currentEl.copy()
                ans.append(copy)
                return
            
            currentEl.append(nums[index])
            traverse(currentEl, index+1, ans)
            currentEl.pop()
            traverse(currentEl, index+1, ans)
        
        traverse([], 0, res)
        return res
