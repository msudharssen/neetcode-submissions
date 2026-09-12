class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == '+':
                stack.append(stack.pop() + stack.pop())
            elif ch == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2-val1)
            elif ch == '*':
                stack.append(stack.pop()*stack.pop())
            elif ch == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2/val1))
            else:
                stack.append(int(ch))
        return stack[-1]
