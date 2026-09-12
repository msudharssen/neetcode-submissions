class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        visited.add((0,0))
        queue = deque()
        queue.append((0,0,1))

        while queue:
            currentR, currentC, length = queue.popleft()
            if currentR == rows-1 and currentC == cols-1:
                return length
            directions = [[1,0],[0,1],[-1,0],[0,-1], [1,1],[1,-1],[-1,-1],[-1,1]]
            for r,c in directions:
                newR, newC = currentR + r, currentC + c
                if newR>=0 and newR < rows and newC >= 0 and newC < cols and (newR,newC) not in visited and grid[newR][newC]==0:
                    queue.append((newR, newC, length+1))
                    visited.add((newR, newC))

        return -1

