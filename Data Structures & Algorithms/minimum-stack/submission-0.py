class MinStack:

    def __init__(self):
        self.info = []
        self.minstack = []
       
        

    def push(self, val: int) -> None:
        self.info.append(val)
        value = min(val, self.minstack[-1] if len(self.minstack)>0 else val)
        self.minstack.append(value)
        

        
        

    def pop(self) -> None:
        self.info.pop()
        self.minstack.pop()


        

        

    def top(self) -> int:
        return self.info[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

        
