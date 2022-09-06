# https://leetcode.com/problems/fibonacci-number/
class Solution:
    # crazy version!
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        smaller = 0
        bigger = 1
        for _ in range(n-1):
            smaller, bigger = bigger, smaller + bigger
        return bigger

    # recursive-ish solution (slower)
    def fib_lame(self, n: int) -> int:
        if n < 2:
            return n
        fib_seq = [0, 1]
        for i in range(2, n+1):
            fib_seq.append(fib_seq[i-2] + fib_seq[i-1])
        return fib_seq[n]
