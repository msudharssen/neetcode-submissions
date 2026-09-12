class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        temp = [0] * 26
        temp2 = [0] * 26

        for ch in s:
            temp[ord(ch)-ord('a')]+=1
        
        for c in t:
            temp2[ord(c)-ord('a')]+=1
        
        print (temp)
        print (temp2)
        return temp==temp2