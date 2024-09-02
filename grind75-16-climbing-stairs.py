# https://leetcode.com/problems/climbing-stairs/
class Solution:
    # Tabulation
    def climbStairs(self, n: int) -> int:
        ways = {1:1, 2:2}
        for steps in range(3, n+1):
            ways[steps] = ways[steps-2] + ways[steps-1]
        return ways[n]

    # Running tabulation - most efficient
    def climbStairs(self, n: int) -> int:
        lower, higher = 1, 1
        for _ in range(n-1):
            lower, higher = higher, lower + higher
        return higher

    # Memoization
    def climbStairs(self, n: int) -> int:
        self.ways = {1: 1, 2: 2}
        return self.climb_stairs(n)

    def climb_stairs(self, n: int) -> int:
        if n not in self.ways:
            self.ways[n] = self.climb_stairs(n-2) + self.climb_stairs(n-1)
        return self.ways[n]
