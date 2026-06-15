# https://leetcode.com/problems/valid-parentheses/
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isValid(self, s: str) -> bool:
        PAREN_MAP = { '(': ')', '[': ']', '{': '}' }
        open_paren_stack = []
        for char in s:
            if char in PAREN_MAP:
                open_paren_stack.append(char)
            elif not open_paren_stack or char != PAREN_MAP[open_paren_stack.pop()]:
                return False
        return not open_paren_stack
