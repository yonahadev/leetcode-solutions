class MinStack:
    #need some kind of way to order minimum elements constant time
    def __init__(self):
        self.stack = []
        self.minimum = float("inf")
    def push(self, val: int) -> None:
        self.stack.append((val, self.minimum))
        self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        toople = self.stack.pop()
        self.minimum = toople[1]
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
