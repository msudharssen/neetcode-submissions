class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        seen = defaultdict(int)
        for ch in s:
            seen[ch]+=1
        
        for ch in t:
            if ch in seen and seen[ch]>0:
                seen[ch]-=1
                if seen[ch]==0:
                    del seen[ch]
            else:
                return False
        return False if seen else True