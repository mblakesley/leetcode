# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    # 97th percentile
    def findAnagrams(self, s: str, p: str) -> list[int]:
        lenp = len(p)
        diff = {ltr: 0 for ltr in set(s + p)}
        for char in p:
            diff[char] += 1  # sum requirements
        for char in s[:lenp]:
            diff[char] -= 1  # subtract 1st sample @ index 0
        starts = [] if any(diff.values()) else [0]  # any diff = not a match

        # this loop is a sliding diff - we drop s[i] & pick up s[i+lenp], resulting in us being at s[i+1]
        for i in range(len(s) - lenp):
            diff[s[i]] += 1  # sample is losing this; it needs 1 more
            diff[s[i+lenp]] -= 1  # sample is gaining this; it needs 1 less
            if not any(diff.values()):
                starts += [i+1]

        return starts
