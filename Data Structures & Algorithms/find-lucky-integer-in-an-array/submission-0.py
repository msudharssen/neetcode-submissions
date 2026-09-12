class Solution:
    def findLucky(self, arr: List[int]) -> int:
        info = Counter(arr)

        maxValue = 0
        for key, value in info.items():
            if key==value:
                maxValue = max(maxValue, key)
        return maxValue if maxValue!=0 else -1