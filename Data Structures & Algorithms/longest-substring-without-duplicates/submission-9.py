class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        info = set()
        l=0
        r=0
        res=0

        if not s:
            return 0

        while r < len(s):
            if s[r] in info:
                while s[r] in info:
                    info.remove(s[l])
                    l+=1
            res = max(res, r-l+1)
            info.add(s[r])
            r+=1
        return res
            
