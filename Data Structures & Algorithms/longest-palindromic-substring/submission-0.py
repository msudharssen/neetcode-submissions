class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        info = set()

        for i in range(len(s)):
            for j in range(1, len(s)+1):
                info.add(s[i:j])
        
        temp = ""
        for word in info:
            if word == word[::-1]:
                if len(word) > len(temp):
                    temp = word
        
        return temp