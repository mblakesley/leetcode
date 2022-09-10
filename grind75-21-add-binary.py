# https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # make it so $a is always longer
        if len(b) > len(a):
            a, b = b, a
        a, b = a[::-1], b[::-1]
        base = 2
        c: list[int] = []
        carry = 0
        for i, a_char in enumerate(a):
            # stupid trick for safe access; gives '' if out of range; the "or" converts '' to 0
            b_char = b[i:i+1] or 0
            sum_ = int(a_char) + int(b_char) + carry
            carry = 0
            # only works for 2-num addition
            if sum_ >= base:
                carry += 1
                sum_ %= base
            c.append(sum_)
        if carry:
            c.append(carry)  # only works for 2-num addition
        return ''.join(map(str, c[::-1]))


    # cheating
    def addBinaryCheating(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
