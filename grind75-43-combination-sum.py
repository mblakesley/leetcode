# https://leetcode.com/problems/combination-sum/
class Solution:
    # super concise backtracking version
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        solutions = []  # list of combo tuples
        sum_combo_stack = [(0, tuple(), tuple(candidates))]  # list of tuples of (sum, combo, remaining candidates)

        while sum_combo_stack:
            sum_, combo, rem_candidates = sum_combo_stack.pop()
            for i, cand in enumerate(rem_candidates):
                next_sum = sum_ + cand
                if next_sum < target:
                    sum_combo_stack += [(next_sum, (*combo, cand), rem_candidates[i:])]
                elif next_sum == target:
                    solutions += [(*combo, cand)]

        return solutions

    # my initial solution, which is hybrid of DFS & backtracking
    # it's kinda weird, and causes some weird "tree" traversal behavior, necessitating the set(tuple())
    def combo_sum_hybrid(self, candidates: list[int], target: int) -> list[list[int]]:
        sum_combos = {0: {tuple()}}  # sum -> set of tuples of combos
        candidates.sort()  # can be sorted now or at very end; here makes it easy to think thru

        for cand in candidates:
            sum_stack = [*sum_combos]
            while sum_stack:  # DFS
                sum_ = sum_stack.pop()
                combos = sum_combos[sum_]  # guaranteed to exist or we wouldn't be here

                next_sum = sum_ + cand
                if next_sum > target:
                    continue
                next_combos = sum_combos.get(next_sum, set())

                next_combos |= {(*combo, cand) for combo in combos}
                sum_combos[next_sum] = next_combos
                sum_stack += [next_sum]

        return sum_combos.get(target) or []
