# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        int_stack = []  # can include results of previous operations
        for token in tokens:
            if token[-1].isdigit():
                result = int(token)
            else:
                int2, int1 = int_stack.pop(), int_stack.pop()
                if token == '+':
                    result = int1 + int2
                elif token == '-':
                    result = int1 - int2
                elif token == '*':
                    result = int1 * int2
                else:
                    result = int(int1 / int2)
            int_stack.append(result)
        return int_stack.pop()

    # I had to include this: Harold's ridiculous 1-liner-ish using eval(), plus a stack within a list comprehension
    def evalRPN(self, tokens):
        stack = []
        [stack.append(int(hackme) if hackme[-1].isdigit() else int(eval(f"{stack.pop(-2)} {hackme} {stack.pop()}"))) for hackme in tokens]
        return stack.pop()
