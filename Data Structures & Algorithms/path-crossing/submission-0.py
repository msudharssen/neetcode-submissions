class Solution:
    def isPathCrossing(self, path: str) -> bool:
        info = set((0,0))

        prev = [0,0]
        info.add((prev[0], prev[1]))
        for ch in path:
            if ch=='N':
                x, y = prev
                prev = [x, y+1]
            if ch == 'S':
                x, y = prev
                prev = [x, y-1]
            if ch == 'W':
                x, y = prev
                prev = [x-1, y]
            if ch == 'E':
                x, y = prev
                prev = [x+1, y]
            print(prev)
            if (prev[0], prev[1]) in info:
                return True
            else:
                info.add((prev[0], prev[1]))
        return False

