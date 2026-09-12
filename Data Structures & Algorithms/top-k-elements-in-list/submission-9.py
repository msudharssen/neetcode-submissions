class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        holdingFrequencies = defaultdict()
        for num in nums:
            if num in holdingFrequencies:
                holdingFrequencies[num]+=1
            else:
                holdingFrequencies[num]=1
        
        reverse = [(b,a) for a,b in holdingFrequencies.items()]
        heapq.heapify(reverse)

        while len(reverse)>k:
            heapq.heappop(reverse)
        
        res = []
        for a, b in reverse:
            res.append(b)
        return res 

