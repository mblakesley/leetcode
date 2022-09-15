# https://leetcode.com/problems/insert-interval/
class Solution:
    # solution is 1*n
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        left, right = [], []
        overlap_start, overlap_end = newInterval
        for interval in intervals:
            curr_start, curr_end = interval
            if curr_end < overlap_start:
                left.append(interval)
            elif overlap_end < curr_start:
                right.append(interval)
            else:
                overlap_start = min(overlap_start, curr_start)
                overlap_end = max(overlap_end, curr_end)
        return left + [overlap_start, overlap_end] + right
