class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [[position[i],speed[i]] for i in range(len(position))]
        arr.sort(key=lambda x:-x[0])
        stack = []
        for item in arr:
            currPosition, currSpeed = item[0], item[1]
            time = (target-currPosition)/currSpeed
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

        