class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l =0
        r = 1
        count = [0] * 26
        res = 0
        maxFreq = 0

        for r in range(len(s)):
            count[ord(s[r])-ord('A')]+=1
            maxFreq = max(maxFreq, count[ord(s[r])-ord('A')])
            windowLength = r - l +1
            if windowLength - maxFreq > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
            
                

        