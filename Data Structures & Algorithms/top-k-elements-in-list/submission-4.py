class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        allFrequencies = Counter(nums)

        reverse = [(v, k) for k, v in allFrequencies.items()]

        heapq.heapify(reverse)

        while len(reverse) > k:
            heapq.heappop(reverse)
        
        answer = []
        for i, j in reverse:
            answer.append(j)
        return answer

            