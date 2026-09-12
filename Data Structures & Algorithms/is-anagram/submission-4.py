class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        temp1 = sorted(s)
        temp2 = sorted(t)

        return temp1 == temp2