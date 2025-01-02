
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

if __name__ == "__main__":
    a = ["push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
    b = [[2],[0],[3],[0],[],[],[],[],[],[],[]]
    minst = MinStack()
    for name, val in zip(a, b):
        method = getattr(minst, name)  # Get the method by name
        print(method(*val))
        print(minst.stack)
