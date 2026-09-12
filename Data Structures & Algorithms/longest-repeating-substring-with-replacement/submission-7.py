class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charArray = [0]*26
        l = 0
        freq = 0

        for r in range(len(s)):
            charArray[ord(s[r])-ord('A')]+=1
            freq = max(freq, charArray[ord(s[r])-ord('A')])
            window = r-l+1
            if window - freq > k:
                charArray[ord(s[l])-ord('A')]-=1
                l+=1
            res = max(res, r-l+1)        
        return res

