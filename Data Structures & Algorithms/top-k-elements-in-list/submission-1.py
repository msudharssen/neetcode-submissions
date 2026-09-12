class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = collections.Counter(nums)
        res = []

        heap = [(v,k) for (k, v) in freq.items()]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        for key, value in heap:
            res.append(value)

        return res

        