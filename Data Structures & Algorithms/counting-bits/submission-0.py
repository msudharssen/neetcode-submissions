class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for b in range(n+1):
            total = 0
            for i in range(32):
                if b & (1 << i):
                    total+=1
            res.append(total)
        return res
