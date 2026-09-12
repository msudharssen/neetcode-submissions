class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        col = len(grid[0])
        visited = set()
        q = deque()

        def bfs(row, column):
            if (row == rows or row < 0 or column == col or column < 0 or (row,column) in visited or grid[row][column]==-1):
                return
            visited.add((row,column))
            q.append([row,column])

        for r in range(rows):
            for c in range(col):
                if grid[r][c]==0:
                    q.append([r,c])
                    visited.add((r,c))

        
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r+1,c)
                bfs(r,c+1)
                bfs(r-1,c)
                bfs(r,c-1)
            dist+=1


        