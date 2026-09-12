class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        first = defaultdict()
        second = defaultdict()

        temp1 = tuple(sorted(s))
        temp2 = tuple(sorted(t))

        first[temp1] = 1
        second[temp2] = 1

        return first == second


        