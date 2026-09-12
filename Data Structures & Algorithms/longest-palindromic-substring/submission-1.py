class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        temp = ""
        for i in range(len(s)):
            for j in range(1, len(s)+1):
                curr = s[i:j]
                if curr == curr[::-1]:
                    if len(curr) > len(temp):
                        temp = curr
        
        return temp