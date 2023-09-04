class MinStack:

    def __init__(self):
        #init two stacks one for tracking values and one for min vals added so far
        self.stack = []
        self.minstack = []
    def push(self, val: int) -> None:
        #take input val and append to first stack
        self.stack.append(val)
        #if already val in min stack take min of input val and top of min stack val
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()