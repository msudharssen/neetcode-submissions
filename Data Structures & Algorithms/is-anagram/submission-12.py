class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        allChars = [0]*26
        for ch in s:
            allChars[ord('a')-ord(ch)]+=1
        for ch in t:
            allChars[ord('a')-ord(ch)]-=1
        return max(allChars)==min(allChars)