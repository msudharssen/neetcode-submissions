class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return None
        rows = len(board)
        cols = len(board[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!='O':
                return
            board[r][c]='T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for i in range(rows):
            for j in range(cols):
                if (i==0 or i==rows-1) and board[i][j]=='O':
                    dfs(i,j)
                elif (j==0 or j==cols-1) and board[i][j]=='O':
                    dfs(i,j)




        for t in range(rows):
            for m in range(cols):
                if board[t][m]=='O':
                    board[t][m]='X'
        
        for a in range(rows):
            for b in range(cols):
                if board[a][b]=='T':
                    board[a][b]='O'

        



        


