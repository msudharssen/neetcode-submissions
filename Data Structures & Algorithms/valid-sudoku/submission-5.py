class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]!='.':
                    if board[r][c] in cols[c]:
                        return False
                    if board[r][c] in rows[r]:
                        return False
                    if board[r][c] in boxes[tuple((r//3, c//3))]:
                        return False
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    boxes[tuple((r//3,c//3))].add(board[r][c])
        return True
