class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        right = 0

        for ch in s:
            if ch=='(':
                left+=1
                right+=1
            elif ch == ')':
                left-=1
                right-=1
            else:
                left-=1
                right+=1
            if right < 0:
                return False
            left = max(left, 0)
        return left == 0