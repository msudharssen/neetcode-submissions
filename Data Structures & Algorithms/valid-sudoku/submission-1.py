class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        colInfo = defaultdict(set)
        rowInfo = defaultdict(set)
        blockInfo = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    temp = tuple([i//3 , j//3])
                    if int(board[i][j]) in colInfo[j] or int(board[i][j]) in rowInfo[i]:
                        return False
                    elif int(board[i][j]) in blockInfo[temp]:
                        return False
                    else:
                        colInfo[j].add(int(board[i][j]))
                        rowInfo[i].add(int(board[i][j]))
                        blockInfo[temp].add(int(board[i][j]))
        
        return True

                
