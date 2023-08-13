# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        PAREN_MAP = { '(': ')', '{': '}', '[': ']' }
        close_paren_stack = []
        for char in s:
            if char in PAREN_MAP:
                close_paren_stack.append(PAREN_MAP[char])
            elif not close_paren_stack or char != close_paren_stack.pop():
                return False
        return not close_paren_stack
