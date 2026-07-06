import heapq

# https://leetcode.com/problems/k-closest-points-to-origin/
class Solution:
    # Ridiculous python 1-liner. Note that this is the only heapq function that accepts a sort key.
    # Time complexity: O(n log k)
    # Space complexity: O(k)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return heapq.nsmallest(k, points, lambda xy: xy[0]**2 + xy[1]**2)

    # Using normal heap functionality without nsmallest()
    # Time complexity: O(n log k)
    # Space complexity: O(k)
    def k_closest_without_nsmallest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = [(x**2 + y**2, x, y) for x, y in points[:k]]  # (z^2, x, y)
        heapq.heapify_max(max_heap)
        for i in range(k, len(points)):
            x, y = points[i]
            heapq.heappushpop_max(max_heap, (x**2 + y**2, x, y))  # pushpop() is more efficient than alternatives
        return [[x, y] for _, x, y in max_heap]

    # Naive 1-liner. It's surprisingly performant compared to naive implementations of a heap!
    # Time complexity: O(n log n)
    # Space complexity: O(n) / O(log n) depending on sort implementation
    def k_closest_without_heap(self, points: list[list[int]], k: int) -> list[list[int]]:
        return sorted(points, key=lambda xy: xy[0]**2 + xy[1]**2)[:k]
