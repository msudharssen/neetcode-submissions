class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        info = defaultdict(list)
        for source, target, time in times:
            info[source].append([target, time])
        
        queue = []
        visited = set()
        res = 0
        queue.append([0,k])
        heapq.heapify(queue)


        while queue:
            cost, node = heapq.heappop(queue)
            if node in visited:
               continue
            visited.add(node)
            res = max(res, cost)
            for target, time in info[node]:
                if target not in visited:
                    updated = cost + time
                    heapq.heappush(queue,(updated, target))
        return res if len(visited) == n else -1
                    


