class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = 0

        def dfs(r,c):
            if r<0 or c<0 or c>=cols or r>=rows or (r,c) in visited or grid[r][c]==0:
                return 0
            
            visited.add((r,c))
            count = 1
            count+=dfs(r-1,c)
            count+=dfs(r+1,c)
            count+=dfs(r,c-1)
            count+=dfs(r,c+1)
            return count
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    res = max(res, dfs(i,j))
        return res
