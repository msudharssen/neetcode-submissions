class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        block = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    if board[i][j] in row[i] or board[i][j] in col[j]:
                        return False 
                    elif board[i][j] in block[tuple((i//3, j//3))]:
                        return False
                    else:
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                        block[tuple((i//3, j//3))].add((board[i][j]))
        
        return True