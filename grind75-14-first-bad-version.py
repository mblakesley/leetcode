# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return True  # placeholder


# https://leetcode.com/problems/first-bad-version/
class Solution:
    def firstBadVersion(self, n: int) -> int:
        lowest_bad: int = n
        lowest_unknown: int = 1

        while lowest_unknown < lowest_bad:
            n = (lowest_bad + lowest_unknown) // 2
            if isBadVersion(n):
                lowest_bad = n
            else:
                lowest_unknown = n + 1
        return lowest_unknown
