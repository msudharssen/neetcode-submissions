class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        info = defaultdict(list)
        for pair in edges:
            info[pair[0]].append(pair[1])
            info[pair[1]].append(pair[0])
        visited = [False] * n

        def dfs(i):
            for ind in (info[i]):
                if not visited[ind]:
                    visited[ind] = True
                    dfs(ind)
        
        for a in range(n):
            if not visited[a]:
                visited[a] = True
                dfs(a)
                res+=1
        return res
            
