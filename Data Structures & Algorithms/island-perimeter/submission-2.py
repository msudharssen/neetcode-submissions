class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        self.perimeter = 0
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            count = 0
            count += dfs(r+1,c)
            count += dfs(r-1,c)
            count += dfs(r,c+1)
            count += dfs(r,c-1)
            return count
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return (dfs(r,c))
        return 0