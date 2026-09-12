class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = Counter(nums)

        for num, frequency in freq.items():
            heap.append([-frequency, num])
        
        heapq.heapify(heap)
        print(heap)
        res = []
        while k > 0:
            f, n = heapq.heappop(heap)
            res.append(n)
            k-=1
        return res