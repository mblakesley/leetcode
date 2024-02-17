# https://leetcode.com/problems/insert-interval/
class Solution:
    # O(n) solution - 70th percentile
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        j, k = 0, len(intervals)
        new_start, new_end = newInterval
        for i, (start, end) in enumerate(intervals):
            if end < new_start:
                j += 1
            elif start <= new_end:
                new_start = min(new_start, start)
                new_end = max(new_end, end)
            else:
                k = i  # we actually want i-1 but python's end boundary is exclusive
                break
        intervals[j:k] = [[new_start, new_end]]
        return intervals
