# https://leetcode.com/problems/implement-queue-using-stacks/
# This Stack class is only described in the problem, but I explicitly wrote it out, just so we're all clear
class Stack:
    stack: list[int]

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def peek(self) -> int:
        return self.stack[-1]

    def pop(self) -> int:
        return self.stack.pop()

    def size(self) -> int:
        return len(self.stack)

    def is_empty(self) -> bool:
        return not self.stack


class MyQueue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def push(self, x: int) -> None:
        self.push_stack.push(x)

    def pop(self) -> int:
        self._flip_if_needed()
        return self.pop_stack.pop()

    def peek(self) -> int:
        self._flip_if_needed()
        return self.pop_stack.peek()

    def empty(self) -> bool:
        return self.push_stack.is_empty() and self.pop_stack.is_empty()

    # This is the trick! Only flip one way, and only when needed.
    def _flip_if_needed(self):
        if self.pop_stack.is_empty():
            while not self.push_stack.is_empty():
                self.pop_stack.push(self.push_stack.pop())
