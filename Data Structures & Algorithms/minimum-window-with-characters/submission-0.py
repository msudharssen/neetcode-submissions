class Solution:
    def minWindow(self, s: str, t: str) -> str:

        secondWord = defaultdict(int)
        firstWord = defaultdict(int)

        for char in t:
            secondWord[char]+=1
        
        have = 0
        req = len(secondWord)
        res = float('inf')
        l = 0
        f = -1
        m = -1

        for r in range(len(s)):
            currentChar = s[r]
            firstWord[currentChar]+=1

            if currentChar in secondWord and firstWord[currentChar]==secondWord[currentChar]:
                have+=1
                while have == req:
                    if (r-l+1) < res:
                        m = r
                        f = l
                        res = (r-l+1)
                    firstWord[s[l]]-=1
                    if s[l] in secondWord and firstWord[s[l]] < secondWord[s[l]]:
                        have-=1
                    l+=1
        
        return s[f:m+1] if res != float('inf') else ""
                

        