class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rSet = defaultdict(list)
        cSet = defaultdict(list)
        block = defaultdict(list)

        for row in range(len(board)):
            for colum in range(len(board[0])):

                if board[row][colum]!='.':
                    if board[row][colum] in rSet[row] or board[row][colum] in cSet[colum]:
                        return False
                    else:
                        rSet[row].append(board[row][colum])
                        cSet[colum].append(board[row][colum])
                    if board[row][colum] in block[tuple([row//3, colum//3])]:
                        return False
                    else:
                        block[tuple([row//3, colum//3])].append(board[row][colum])
        
        return True



        