class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #all input is valid
        #not all input will have a valid solution
        #rows <= 100, cols <=100 -> Constraints
        #land - 1 , water - 0

        #Approach -> run a dfs on every cell that is a land (1)
        #For each adjacent ones, up the count, if the count returned is greater than
        #1> -> thats a valid path, count it as 1, if its equal to 1 -> stil count it as 1

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == "0":
                return 
            
            visited.add(tuple([r,c]))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r,c-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    res+=1
        return res


