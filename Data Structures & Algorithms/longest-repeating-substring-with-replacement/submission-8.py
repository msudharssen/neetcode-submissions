class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        subString = defaultdict(int)
        maxFreq = 0
        l = 0

        for r in range(len(s)):
            subString[s[r]]+=1
            maxFreq = max(maxFreq, subString[s[r]])
            while r-l+1 - maxFreq >k:
                subString[s[l]]-=1
                l+=1
            res = max(res, r-l+1)

        return res
                

