class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in visited or grid[r][c]==0:
                return 0
            
            visited.add((r,c))
            count = 1
            count += dfs(r+1, c)
            count += dfs(r-1,c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)
            return count
        
        maxArea = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    maxArea = max(maxArea, dfs(row,col))
        return maxArea