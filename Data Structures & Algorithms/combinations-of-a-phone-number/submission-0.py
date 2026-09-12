class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        info = defaultdict(str)
        info['2'] = 'abc'
        info['3'] = 'def'
        info['4'] = 'ghi'
        info['5'] = 'jkl'
        info['6'] = 'mno'
        info['7'] = 'pqrs'
        info['8'] = 'tuv'
        info['9'] = 'wxyz'

        def dfs(arr, ind, dit, nums):
            if ind == len(nums):
                temp = "".join(arr)
                res.append(temp)
                return
            
            val = dit[nums[ind]]
            for v in val:
                arr.append(v)
                dfs(arr, ind+1, dit, nums)
                arr.pop()
        
        dfs([], 0, info, digits)
        print(res)
        return res
