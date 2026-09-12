class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        total = 0
        count = [0] * 26
        l = 0
        maxFreq = 0

        for r in range(len(s)):
            count[ord(s[r])-ord('A')]+=1
            maxFreq = max(maxFreq, count[ord(s[r])-ord('A')])
            if (r-l+1) - maxFreq>k:
                count[ord(s[l])-ord('A')]-=1
                l+=1
            total = max(r-l+1, total) 
        
        return total
        