class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        res = 0
        maxHeap = [ -count for count in count.values()]
        heapq.heapify(maxHeap)
        queue = deque()

        while maxHeap or queue:
            res+=1
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count!=0:
                    queue.append([count, res+n])
            if queue and queue[0][1]==res:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return res




