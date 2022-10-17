# https://leetcode.com/problems/coin-change/
class Solution:
    # Magical "breadth-first search" version
    def coinChange(self, coins: list[int], amount: int) -> int:
        if not amount:
            return 0

        totals = {0: 0}  # total amount -> min count
        totals_queue = [0]
        while totals_queue:
            total = totals_queue.pop(0)
            min_count = totals[total]
            for coin in coins:
                new_total = total + coin

                if new_total < amount:
                    # if we've seen it before, BFS guarantees original path was shortest
                    if new_total in totals:
                        continue
                    totals[new_total] = min_count + 1
                    totals_queue.append(new_total)

                elif new_total == amount:
                    # we can just return immediately, since BFS guarantees shortest path
                    return min_count + 1
        return -1


    # Slightly less magical "dynamic programming" version
    # Leetcode says this is slower than a "look-behind" version, but this is easier to read / think about
    def coinChange(self, coins: list[int], amount: int) -> int:
        totals = {0: 0}  # total amount -> min count

        # note: "count" is guaranteed to be min for amounts <= total, but not for amounts > total
        for total in range(amount + 1):
            min_count = totals.get(total)
            if min_count is None:
                continue

            for coin in coins:
                higher_total = total + coin
                higher_min_count = totals.get(higher_total)
                if higher_min_count is None:
                    totals[higher_total] = min_count + 1
                else:
                    totals[higher_total] = min(higher_min_count, min_count + 1)

        if amount in totals:
            return totals.get(amount)
        return -1


    # terrible, horrible approach that tries to find all combos
    def WASTE_OF_MY_FUCKING_TIME(self, coins: list[int], amount: int) -> int:
        coin_sizes = sorted(coins, reverse=True)  # sort coins big to small
        size_count = len(coin_sizes)
        target = amount
        min_len = target + 1  # impossibly high value
        coin_stack = []
        diff = target

        # initial pass - add AMAP, biggest first
        for size in coin_sizes:
            div, mod = divmod(diff, size)
            coin_stack += [size] * div
            diff = mod
            if not diff:
                min_len = min(min_len, len(coin_stack))
                break

        # back off a coin bigger than smallest coin
        while coin_stack:
            last_coin = coin_stack.pop()
            diff += last_coin
            if last_coin == coin_sizes[-1]:
                continue

            # set coin size to smaller than the popped coin, then retry adding
            i = coin_sizes.index(last_coin) + 1
            # add AMAP, biggest first
            while i < size_count:
                size = coin_sizes[i]
                div, mod = divmod(diff, size)
                coin_stack += [size] * div
                diff = mod
                if not diff:
                    min_len = min(min_len, len(coin_stack))
                    break
                i += 1

        return min_len if min_len != target + 1 else -1
