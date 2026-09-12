class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        allVals = Counter(nums)

        reverse = [(freq, numb) for numb, freq in allVals.items()]

        heapq.heapify(reverse)

        while len(reverse) > k:
            heapq.heappop(reverse)
        
        return list(numb for key, numb in reverse)
        