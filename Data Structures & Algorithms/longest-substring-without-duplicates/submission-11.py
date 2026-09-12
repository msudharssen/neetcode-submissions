class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        info = set()
        l = 0
        res = float('-inf')

        for r in range(len(s)):
            if s[r] in info:
                while s[r] in info:
                    info.remove(s[l])
                    l+=1
            info.add(s[r])
            res = max(res, r-l+1)
        return res if res!=float('-inf') else 0