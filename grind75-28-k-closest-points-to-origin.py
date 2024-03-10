import heapq


# https://leetcode.com/problems/k-closest-points-to-origin/
class Solution:
    # O(n log k) using heap, 1-liner
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return heapq.nsmallest(k, points, lambda xy: xy[0]**2 + xy[1]**2)

    # O(n log k) using heap, done more manually to learn about heaps
    def kClosest_heap_long(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = [(-x**2 - y**2, x, y) for x, y in points[:k]]
        heapq.heapify(heap)
        for x, y in points[k:]:
            sum_ = -x**2 - y**2
            if sum_ > heap[0][0]:
                heapq.heapreplace(heap, (sum_, x, y))
        return [[x, y] for _, x, y in heap]

    # O(n log n) Mega naive 1-liner that's surprisingly performant, at least on leetcode's dataset
    # As in, it's MUCH more performant than writing out a naive implementation of a heap.
    def kClosest_kn(self, points: list[list[int]], k: int) -> list[list[int]]:
        return sorted(points, key=lambda xy: xy[0]**2 + xy[1]**2)[:k]
