class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for astroid in asteroids:
            while stack and astroid < 0 and stack[-1]>0:
                    change = astroid + stack[-1]
                    if change < 0:
                        stack.pop()
                    elif change > 0:
                        astroid = 0
                    else:
                        astroid = 0
                        stack.pop()
            if astroid:
                stack.append(astroid)
        return stack