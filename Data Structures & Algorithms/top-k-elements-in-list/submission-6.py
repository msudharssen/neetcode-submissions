class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        info = Counter(nums)

        reverse = [(a,b) for b, a in info.items()]
        

        heapq.heapify(reverse)
        print(reverse)

        while len(reverse) > k:
            heapq.heappop(reverse)
        
        return list(b for a,b in reverse)