class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = [0] * 26
        l = 0
        freq = 0

        for r in range(len(s)):
            count[ord(s[r])-ord('A')]+=1
            freq = max(freq, count[ord(s[r])-ord('A')])
            windowLength = r - l +1
            if windowLength - freq > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
