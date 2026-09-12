class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        info = defaultdict(list)
        for time in times:
            source, target, duration = time
            info[source].append([target, duration])
        
        minHeap = [(0,k)]
        visited = set()
        heapq.heapify(minHeap)
        res = 0

        while minHeap:
            path, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, path)
            for neigh, time in info[node]:
                updatedPath = path + time
                if neigh not in visited:
                    heapq.heappush(minHeap,(updatedPath, neigh))
        return res if len(visited)==n else -1











