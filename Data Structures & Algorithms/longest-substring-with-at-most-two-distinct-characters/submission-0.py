class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        res = 0
        chars = defaultdict(int)

        for r in range(len(s)):
            chars[s[r]]+=1
            while len(chars)>2:
                chars[s[l]]-=1
                if chars[s[l]]==0:
                    chars.pop(s[l])
                l+=1
            res = max(res, r-l+1)
        return res
