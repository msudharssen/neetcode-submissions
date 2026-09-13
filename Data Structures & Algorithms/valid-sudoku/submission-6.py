class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return True

        rows = defaultdict(set)
        cols = defaultdict(set)
        block = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col]!='.':
                    if board[row][col] in rows[row]:
                        return False
                    if board[row][col] in cols[col]:
                        return False
                    if board[row][col] in block[tuple((row//3, col//3))]:
                        return False
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    block[tuple((row//3, col//3))].add(board[row][col])
        return True
            

