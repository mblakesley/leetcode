# https://leetcode.com/problems/valid-anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return analyze_ltr_dist(s) == analyze_ltr_dist(t)


def analyze_ltr_dist(s: str) -> dict[str, int]:
    """Given a string, return a dict of its letter distribution"""
    ltr_dist: dict[str, int] = {}
    for char in s:
        if char in ltr_dist:
            ltr_dist[char] += 1
        else:
            ltr_dist[char] = 1
    return ltr_dist
