# https://leetcode.com/problems/min-stack/
class MinStack:
    stack: list
    min_stack: list

    def __init__(self):
        self.stack = []
        self.min_stack = []  # but, like, a stack of mins, not a MinStack

    def push(self, n: int) -> None:
        self.stack.append(n)
        if not self.min_stack or n <= self.min_stack[-1]:
            self.min_stack.append(n)

    def pop(self) -> int:
        n = self.stack.pop()
        if self.min_stack and n == self.min_stack[-1]:
            self.min_stack.pop()
        return n

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
