class Solution:
    def maxDifference(self, s: str) -> int:
        info = Counter(s)
        odd = 0
        even = float('inf')

        for val in info.values():
            if val%2!=0:
                odd = max(odd, val)
            else:
                even = min(even, val)
        return odd - even