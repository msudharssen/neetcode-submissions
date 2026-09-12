class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        first = defaultdict()

        temp1 = tuple(sorted(s))
        temp2 = tuple(sorted(t))

        
        return temp1 == temp2