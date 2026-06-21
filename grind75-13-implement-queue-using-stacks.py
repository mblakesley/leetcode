# https://leetcode.com/problems/implement-queue-using-stacks/
# I explicitly wrote out a Stack class to keep me honest
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
        self.forwards_stack = Stack()
        self.backwards_stack = Stack()

    def push(self, x: int) -> None:
        self.forwards_stack.push(x)

    def pop(self) -> int:
        self._flip_if_needed()
        return self.backwards_stack.pop()

    def peek(self) -> int:
        self._flip_if_needed()
        return self.backwards_stack.peek()

    def empty(self) -> bool:
        return self.forwards_stack.is_empty() and self.backwards_stack.is_empty()

    # This is the trick! Only flip when needed!
    def _flip_if_needed(self):
        if self.backwards_stack.is_empty():
            while not self.forwards_stack.is_empty():
                self.backwards_stack.push(self.forwards_stack.pop())
