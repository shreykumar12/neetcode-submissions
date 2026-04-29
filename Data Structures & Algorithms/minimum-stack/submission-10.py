class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or self.minstack[-1] >= val:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()

            
        
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        return self.minstack[-1]
