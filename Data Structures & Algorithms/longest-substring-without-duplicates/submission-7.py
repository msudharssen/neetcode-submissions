class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        l=0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l+=1
            hashSet.add(s[r])
            maxLength = max(maxLength, len(hashSet))
        return maxLength

