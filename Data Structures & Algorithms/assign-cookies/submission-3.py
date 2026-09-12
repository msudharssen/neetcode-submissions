class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        l = 0
        r = 0
    
        while l < len(g) and r < len(s):
            while r < len(s) and g[l] > s[r]:
                r+=1
            if r == len(s):
                break
            else:
                l+=1
                r+=1
        return l
            

            