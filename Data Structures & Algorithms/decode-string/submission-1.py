class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        for ch in s:
            if ch!=']':
                stack.append(ch)
            else:
                curr = ''
                while stack and stack[-1]!='[':
                    curr = stack.pop() + curr
                stack.pop()
                number = ''
                while stack and stack[-1].isdigit():
                    number = stack.pop()+ number
                curr = int(number) * curr
                stack.append(curr)
        return "".join(stack)

                    
