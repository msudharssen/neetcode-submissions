class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(first, openBracket, closeBracket, n, info):
            if openBracket==closeBracket==n:
                info.append(first)
                return
            if openBracket < n:
                backtrack(first+"(", openBracket+1, closeBracket, n, info)
            if closeBracket < openBracket:
                backtrack(first+")", openBracket, closeBracket+1, n, info)
        info = []
        backtrack("", 0,0,n,info)
        return info  




        