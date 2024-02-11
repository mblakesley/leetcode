# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    # O(n) solution using queue + set (which could easily be modified to return the substring itself)
    # There's a 2x faster solution using only a dict of {char: index} but it loses track of the actual substring
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque  # Only 'cuz python lacks a built-in queue
        char_queue = deque()
        uniques = set()
        max_len = 0
        for char in s:
            if char in uniques:
                max_len = max(max_len, len(uniques))
                while char_queue[0] != char:
                    uniques.discard(char_queue.popleft())
                char_queue.popleft()
            char_queue.append(char)
            uniques.add(char)
        return max(max_len, len(uniques))

    # Cuter but less performant
    # O(k*n) where k can vary but should be proportional to the number of unique chars
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        max_len = 0
        for char in s:
            if char in substr:
                max_len = max(max_len, len(substr))
                substr = substr.split(char)[-1]
            substr += char
        return max(max_len, len(substr))
