# https://leetcode.com/problems/implement-queue-using-stacks/
# This Stack class is only described in the problem, but I explicitly wrote it out, just so we're all clear
class Stack:
    _stack: list[int]

    def __init__(self):
        self._stack = []

    def push(self, x: int) -> None:
        self._stack.append(x)

    def peek(self) -> int:
        return self._stack[-1]

    def pop(self) -> int:
        return self._stack.pop()

    def size(self) -> int:
        return len(self._stack)

    def empty(self) -> bool:
        return not self._stack


class MyQueue:
    _stack: Stack
    _rev_stack: Stack

    def __init__(self):
        self._stack = Stack()
        self._rev_stack = Stack()

    def push(self, x: int) -> None:
        """append"""
        self._stack.push(x)

    def pop(self) -> int:
        """from front"""
        self._flip_stacks()
        return self._rev_stack.pop()

    def peek(self) -> int:
        self._flip_stacks()
        return self._rev_stack.peek()

    def _flip_stacks(self) -> None:
        if self._rev_stack.empty():
            while not self._stack.empty():
                self._rev_stack.push(self._stack.pop())

    def empty(self) -> bool:
        return self._stack.empty() and self._rev_stack.empty()
