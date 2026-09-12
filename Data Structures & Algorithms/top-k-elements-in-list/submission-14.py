class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = Counter(nums)

        heap = []

        for num, freq in frequencies.items():
            heap.append([-freq, num])
        
        heapq.heapify(heap)

        res = []

        while k!=0:
            amount, numb = heapq.heappop(heap)
            res.append(numb)
            k-=1
        
        return res