class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()
        fresh = 0
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append((i,j))
        

        while fresh > 0 and queue:
            for k in range(len(queue)):
                r,c = queue.popleft()
                
                directions = [[1,0], [-1,0], [0,-1], [0,1]]
                for direct in directions:
                    changedR = direct[0]+r
                    changedC = direct[1]+c

                    if changedR >= 0 and changedC >= 0 and changedR < rows and changedC < cols and (changedR, changedC) not in visited and grid[changedR][changedC]==1:
                        queue.append((changedR, changedC))
                        visited.add((changedR, changedC))
                        fresh-=1
            res+=1
        
        return res if fresh == 0 else -1