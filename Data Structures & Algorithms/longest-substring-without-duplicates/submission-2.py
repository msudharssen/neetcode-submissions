class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = set()
        first = 0
        maxLen = 0

        
        for i in range(len(s)):
            while s[i] in ans:
                ans.remove(s[first])
                first+=1
            ans.add(s[i])
            maxLen = max(maxLen, i-first+1)
        return maxLen