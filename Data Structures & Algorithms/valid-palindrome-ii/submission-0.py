class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        def palindrome(s):
            left = 0
            right = len(s)-1

            while left < right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        while l < r:
            if s[l]!=s[r]:
                leftWord, rightWord = s[l+1:r+1],s[l:r]
                return palindrome(leftWord) or palindrome(rightWord)
            l+=1
            r-=1
        return True