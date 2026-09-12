class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characterArrayS = [0] * 26
        characterArrayT = [0] * 26

        for ch in s:
            characterArrayS[ord(ch)-ord('a')]+=1
        
        for ch in t:
            characterArrayT[ord(ch)-ord('a')]+=1
        
        return characterArrayS==characterArrayT
