class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        info = defaultdict(int)
        res = 0
        l = 0
        freq = 0

        for r in range(len(s)):
            info[s[r]] = info[s[r]]+1
            freq = max(freq, info[s[r]])
            while (r-l+1) - freq > k:
                info[s[l]]-=1
                l+=1
            res = max(res, (r-l+1))
        return res
