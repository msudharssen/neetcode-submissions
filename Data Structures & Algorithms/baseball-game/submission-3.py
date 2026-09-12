class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, res = [], 0
        for ch in operations:
            if ch == "+":
                res += stack[-1]+stack[-2]
                stack.append(stack[-1]+stack[-2])
            elif ch == "D":
                res += (stack[-1]*2)
                stack.append(stack[-1]*2)
            elif ch == "C":
                res-=stack.pop()
            else:
                res+=int(ch)
                stack.append(int(ch))
        return res
