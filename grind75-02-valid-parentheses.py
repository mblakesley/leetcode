# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        paren_map: dict = { '(': ')', '{': '}', '[': ']' }
        paren_queue: list[str] = []
        for char in s:
            if char in '({[':
                paren_queue.append(paren_map[char])  # add complement paren
                continue
            # 1st condition here: we got a close paren without a previous open paren
            if not paren_queue or char != paren_queue.pop():
                return False
        # only return True if queue is empty after string is processed
        return not paren_queue
