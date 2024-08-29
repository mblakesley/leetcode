# https://leetcode.com/problems/min-stack/
class MinStack:
    stack: list
    min_stack: list

    def __init__(self):
        self.stack = []
        self.min_stack = []  # dupes included

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> int:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
