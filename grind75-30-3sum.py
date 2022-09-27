# https://leetcode.com/problems/3sum/
class Solution:
    # O(n^2) speed
    def threeSum(self, nums: list[int]) -> set[tuple]:
        target_sum = 0
        counter = {}  # num -> count, BUT count stops incrementing at max of 3
        triplets = set()
        for i, num_i in enumerate(nums):
            count = counter.get(num_i, 0)
            if count == 3:
                continue
            counter[num_i] = count + 1
            # 2-sum problem
            couples = self.two_sum(nums=nums[0:i], target_sum=target_sum - num_i)
            for num_j, num_k in couples:
                triplets.add(tuple(sorted((num_i, num_j, num_k))))
        return triplets

    def two_sum(self, nums: list[int], target_sum: int) -> set[tuple]:
        couples = set()
        complements = set()
        for x in nums:
            y = target_sum - x
            if y in complements:
                couples.add(tuple(sorted((x, y))))
            complements.add(x)
        return couples

    # O(n^2) but monolithic & messy
    def three_sum_monolithic(self, nums: list[int]) -> set[tuple[int]]:
        target_sum = 0
        past_singles = {}  # num -> (first index, count), BUT count stops incrementing at max of 3
        triplets = set()
        # i leads, j follows
        for i, num_i in enumerate(nums):
            first_index, count = past_singles.get(num_i, (i, 0))
            if count == 3:
                continue
            for j in range(0, i):
                num_j = nums[j]
                num_k = target_sum - num_i - num_j
                # 2nd check here: j can re-assume old singles, so make sure num_k's index != j
                if num_k in past_singles and past_singles[num_k][0] != j:
                    triplets.add(tuple(sorted([num_i, num_j, num_k])))
            past_singles[num_i] = (first_index, count + 1)
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
