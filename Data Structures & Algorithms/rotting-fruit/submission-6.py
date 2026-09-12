class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        totalOranges = 0
        queue = deque()
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    totalOranges+=1
                if grid[r][c]==2:
                    queue.append((r,c))
        
        
        while queue and totalOranges>0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                directions = [[0,1], [0,-1],[1,0],[-1,0]]
                for direction in directions:
                    newDr, newDc = row+direction[0], col+direction[1]
                    if newDr>=0 and newDc>=0 and newDr<rows and newDc<cols and grid[newDr][newDc]==1:
                        totalOranges-=1
                        grid[newDr][newDc]=2
                        queue.append((newDr, newDc))
            time+=1
       
        return time if totalOranges == 0 else -1