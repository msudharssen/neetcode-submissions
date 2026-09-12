class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i, temp):
            if i==len(temp):
                return True
            if r < 0 or c < 0 or r>=ROWS or c>=COLS or board[r][c]!=temp[i] or (r,c) in visited:
                return False
            
            visited.add((r,c))
            res = (dfs(r+1, c, i+1, temp) or dfs(r-1, c, i+1, temp) or dfs(r, c+1, i+1, temp) or dfs(r,c-1,i+1, temp))
            visited.remove((r,c))
            return res
        res = set()
        for k in range(len(words)):
            for i in range(ROWS):
                for j in range(COLS):
                    if dfs(i,j,0, words[k]):
                        res.add(words[k])
        
        return list(res)