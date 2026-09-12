class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        info = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            info[s[r]]+=1
            while len(info)>k:
                info[s[l]]-=1
                if not info[s[l]]:
                    del info[s[l]]
                l+=1
            res = max(res, r-l+1)
        return res