class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        info = Counter(nums)

        reverse = [(v, k)  for k, v in info.items()]

        heapq.heapify(reverse)
        answer = []

        while len(reverse) > k:
            heapq.heappop(reverse)
        
        for k, v in reverse:
            answer.append(v)
        
        return answer

