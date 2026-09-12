class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        setOfChars = set()
        l = 0

        for r in range(len(s)):
            if s[r] in setOfChars:
                while s[r] in setOfChars:
                    setOfChars.remove(s[l])
                    l+=1
            setOfChars.add(s[r])
            windowLength = (r-l)+1
            longest = max(longest, windowLength)
        return longest