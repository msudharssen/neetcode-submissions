class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        newN = n+1
        res = [[0]* n for i in range(m)]

        cols = n
        rows = m
        res[rows-1][cols-1] = 1
        
        for i in range(len(res)-1,-1,-1):
            for j in range(len(res[0])-1,-1,-1):
                if i==len(res)-1 and j == len(res[0])-1:
                    print(i,j)
                    res[i][j]=1
                else:
                    rightCol = True if j+1 < len(res[0]) else False
                    rowBelow = True if i+1 < len(res) else False
                    if rightCol and rowBelow:
                        res[i][j] = res[i][j+1]+res[i+1][j]
                    if rightCol and not rowBelow:
                        res[i][j]= res[i][j+1]
                    if rowBelow and not rightCol:
                        res[i][j]=res[i+1][j]
        print(res)
        return res[0][0]

