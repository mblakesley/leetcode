# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        zine_chars: dict = {}
        for char in magazine:
            if char in zine_chars:
                zine_chars[char] += 1
            else:
                zine_chars[char] = 1

        for char in ransomNote:
            if not zine_chars.get(char):
                return False
            zine_chars[char] -= 1

        return True
