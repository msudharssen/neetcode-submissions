class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        subString = set()
        l = 0

        for r in range(len(s)):
            while s[r] in subString:
                subString.remove(s[l])
                l+=1
            subString.add(s[r])
            res = max(res, len(subString))
        return res