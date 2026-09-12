class MedianFinder:

    def __init__(self):
        self.info = []
        

    def addNum(self, num: int) -> None:
        self.info.append(num)
        self.info.sort()
        

    def findMedian(self) -> float:
        even = False
        if len(self.info) % 2 == 0:
            even = True
        ind = len(self.info) // 2
        if not even:
            return (self.info[ind])
        else:
            return float(((self.info[ind]) + self.info[ind-1])/2)

        
        