class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimums_stack and self.minimums_stack[-1] < val:
            self.minimums_stack.append(self.minimums_stack[-1])
        else:
            self.minimums_stack.append(val)

    def pop(self) -> None:
        if self.stack :
            self.stack.pop()
            self.minimums_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums_stack[-1] if self.minimums_stack else int()
