# https://leetcode.com/problems/valid-anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(n)
        return ltr_count_map(s) == ltr_count_map(t)

def ltr_count_map(s: str) -> dict:
    ltr_counts = {}  # {letter: count}
    for char in s:
        count: int = ltr_counts.get(char, 0)
        ltr_counts[char] = count + 1
    return ltr_counts
