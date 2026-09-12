class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculateDistance(x1,y1):
            xVal = abs(x1-0)
            yVal = abs(y1-0)
            xVal*=xVal
            yVal*=yVal
            return xVal+yVal
        
        array = []
        res = []
        for point in points:
            x, y = point
            distance = calculateDistance(x,y)
            array.append([distance, x, y])
        
        heapq.heapify(array)

        while k!=0:
            toAdd = heapq.heappop(array)
            res.append([toAdd[1], toAdd[2]])
            k-=1
        return res
        

        