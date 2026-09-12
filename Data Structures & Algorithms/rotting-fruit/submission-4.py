class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        rottenFruits = []
        visited = set()

        totalFruits = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    totalFruits+=1
                elif grid[i][j]==2:
                    rottenFruits.append((i,j))
        time = 0
        while rottenFruits and totalFruits > 0:
            for i in range(len(rottenFruits)):
                currentR, currentC = rottenFruits.pop(0)
                visited.add((currentR, currentC))
                directions = [[0,1], [1,0], [-1,0], [0,-1]]
                for dr, dc in directions:
                    newR = dr+currentR
                    newC = dc+currentC
                    if newR >= 0 and newC >=0 and newR < rows and newC<cols and (newR, newC) not in visited and grid[newR][newC]==1:
                        totalFruits-=1
                        visited.add((newR, newC))
                        rottenFruits.append((newR, newC))
            time+=1
        return time if totalFruits==0 else -1   

                    

