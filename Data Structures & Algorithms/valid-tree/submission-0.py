class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n ==0:
            return True
        
        info = defaultdict(list)
        for pair in edges:
            info[pair[0]].append(pair[1])
            info[pair[1]].append(pair[0])
        visited = set()
            
        def dfs(d, prev):
            if d in visited:
                return False
            
            
            visited.add(d)
            for ind in info[d]:
                if ind == prev:
                    continue
                if not dfs(ind, d):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visited)
            



        