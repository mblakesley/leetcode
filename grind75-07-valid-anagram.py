# https://leetcode.com/problems/valid-anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return count_letters(s) == count_letters(t)


def count_letters(s: str) -> dict[str, int]:
    """Given a string, return a dict of its letter distribution"""
    ltr_counts = {}
    for char in s:
        count = ltr_counts.get(char, 0)
        ltr_counts[char] = count + 1
    return ltr_counts
