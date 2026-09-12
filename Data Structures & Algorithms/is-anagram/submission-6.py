class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        firstWord = Counter(s)
        secondWord = Counter(t)

        return firstWord == secondWord