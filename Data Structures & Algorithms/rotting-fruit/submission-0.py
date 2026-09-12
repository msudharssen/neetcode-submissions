class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        rotten = deque()
        fresh = 0
        time = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    rotten.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        while rotten and fresh > 0:
            for i in range(len(rotten)):
                temp = rotten.popleft()
                for direction in directions:
                    a, b = temp[0]+direction[0], temp[1]+direction[1]
                    if a < 0 or b < 0 or a>=ROWS or b >= COLS or grid[a][b]!=1:
                        continue
                    grid[a][b] = 2
                    rotten.append([a,b])
                    fresh-=1
            time+=1
        
        return time if fresh==0 else -1




