class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        total = 0

        def bfs(r,c):
            if r < 0 or c < 0 or r>= rows or c>=cols or (r,c) in seen or grid[r][c]!='1':
                return
            
            seen.add((r,c))
            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c+1)
            bfs(r,c-1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in seen:
                    bfs(r, c)
                    total+=1
        
        return total