class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        visited = set()
        queue = []
        res = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    fresh+=1
                elif grid[row][col]==2:
                    queue.append((row,col))
        
        while fresh > 0 and queue:
            for i in range(len(queue)):
                currRow, currCol = queue.pop(0)
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for direct in directions:
                    nextRow, nextCol = currRow+direct[0], currCol+direct[1]
                    if nextRow >=0 and nextCol >=0 and nextRow < rows and nextCol < cols and (nextRow,nextCol) not in visited and grid[nextRow][nextCol]==1:
                        queue.append((nextRow, nextCol))
                        visited.add((nextRow, nextCol))
                        fresh-=1
            res+=1
        return res if fresh==0 else -1
