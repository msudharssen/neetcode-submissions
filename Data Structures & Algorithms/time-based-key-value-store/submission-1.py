class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''
        
        allValues = self.map[key]
        start = 0
        end = len(allValues)-1
        res = ""
        while start <= end:
            mid = (start + end)//2
            if allValues[mid][1]<=timestamp:
                res = allValues[mid][0]
                start = mid+1
            else:
                end=mid-1
        return res




        
