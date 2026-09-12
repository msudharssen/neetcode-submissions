class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        colInfo = defaultdict(set)
        rowInfo = defaultdict(set)
        blockInfo = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    temp = tuple([i//3 , j//3])
                    if (board[i][j]) in colInfo[j] or (board[i][j]) in rowInfo[i]:
                        return False
                    elif (board[i][j]) in blockInfo[temp]:
                        return False
                    else:
                        colInfo[j].add((board[i][j]))
                        rowInfo[i].add((board[i][j]))
                        blockInfo[temp].add((board[i][j]))
        
        return True

                
