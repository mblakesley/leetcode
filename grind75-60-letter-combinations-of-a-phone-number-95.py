# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    num_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    # 95th percentile
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        combos = [ltr for ltr in self.num_map[digits[0]]]
        for digit in digits[1:]:
            ltrs = self.num_map[digit]
            combos = [combo + ltr for combo in combos for ltr in ltrs]
        return combos
