class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            temp = res[-1][1]
            if intervals[i][0] <= temp:
                res[-1][1] = max(temp, intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res

