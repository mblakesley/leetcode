# https://leetcode.com/problems/3sum/
class Solution:
    # O(n^2) on speed
    def threeSum(self, nums: list[int]) -> set[tuple]:
        target_sum = 0
        counter = {}  # num -> count (count stops incrementing at max of 3)
        triplets = set()
        for i, x in enumerate(nums):
            # skip nums if we've seen them twice before (only 0's can appear thrice - see below)
            count = counter.get(x, 0)
            counter[x] = count + 1
            if count > 2:
                continue

            # 2-sum problem
            complements = {}  # {complement: old y}
            for y in nums[0:i]:
                if y in complements:
                    # this inner loop works by looking backwards, so curr y is actually z, old y is y
                    triplets |= {tuple(sorted((x, complements[y], y)))}
                complements[target_sum - x - y] = y

        if counter.get(0, 0) >= 3:
            triplets |= {(0, 0, 0)}
        return triplets

    # O(n^2 + 2n) on speed BUT uses a weird approach to better filter out extra nums
    def three_sum_no_sorting(self, nums: list[int]) -> set[tuple]:
        # first, compress $nums down to singles & pairs (but don't sort). [2,1,2,3,2] -> [2,2,1,3]
        # we don't care what the absolute order is as long as there is one. this eliminates the need to sort triplets.
        # this process is O(2*n) on speed
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        filtered_nums = []
        for num, count in counter.items():
            filtered_nums += [num] * min(count, 2)

        # now, do 3 sum without sorting! O(n^2)
        triplets = set() if counter.get(0, 0) < 3 else {(0, 0, 0)}  # special case: three 0's
        target_sum = 0
        for i, x in enumerate(filtered_nums):
            # 2 sum problem
            complements = {}  # {complement: old y}
            for y in filtered_nums[i+1:]:
                if y in complements:
                    triplets |= {(x, complements[y], y)}  # this inner loop looks backwards, so old y is y, new y is z
                else:
                    complements[target_sum - x - y] = y
        return triplets


    # super naive O(n^3), for reference
    def three_sum_naive(self, nums: list[int]) -> set[tuple[int]]:
        target_sum = 0
        triplets = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == target_sum:
                        triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return triplets
