class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        info = Counter(nums)
        withSorts=[(val,key) for key, val in info.items()]

        heapq.heapify(withSorts)

        while len(withSorts)!=k:
            heapq.heappop(withSorts)
        
        output = []
        for item in withSorts:
            output.append(item[1])
        return output
        
