class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        first = Counter(s1)
        l = 0

        
        for r in range(len(s1), len(s2)+1):
            temp = s2[l:r]
            freq = Counter(temp)
            same = True
            for key, val in freq.items():
                if key not in first or freq[key] != first[key]:
                    same = False
            if same:
                return True 
            else:
                l+=1
                r+=1
                        
        return False