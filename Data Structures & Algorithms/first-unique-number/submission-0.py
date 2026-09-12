class FirstUnique:

    def __init__(self, nums: List[int]):
        self.vals = defaultdict(int)
        self.allVals = deque(nums)
        for num in nums:
            self.vals[num]+=1

    def showFirstUnique(self) -> int:
        while self.allVals and self.vals[self.allVals[0]]!=1:
            self.allVals.popleft()
        
        if self.allVals:
            return self.allVals[0]
        return -1

    def add(self, value: int) -> None:
        self.vals[value]+=1
        self.allVals.append(value)

        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
