class Solution:
    def countElements(self, arr: List[int]) -> int:
        info = set(arr)
        res = 0

        for num in arr:
            if num + 1 in info:
                res+=1
        return res
            