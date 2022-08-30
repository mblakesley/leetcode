class Solution:
    # generalized solution
    # can handle negative prices, also min's losses if applicable
    # this algo is re-used in "maximum-subarray"
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0

        # min has to be the first value seen, rather than 0
        p_min: int = prices[0]
        max_profit: int = prices[1] - prices[0]

        for price in prices[1:]:
            profit: int = price - p_min
            max_profit = max(max_profit, profit)
            p_min = min(p_min, price)

        # would return min loss, but instructions say "return max profit or 0"
        return max_profit if max_profit > 0 else 0


    # # naive solution - doesn't handle negative prices nor does it minimize losses
    # def maxProfit(self, prices: list[int]) -> int:
    #     # min has to be the first value seen, rather than 0
    #     p_min: int = prices[0]
    #     max_profit: int = 0
    #
    #     for price in prices:
    #         if price < p_min:
    #             p_min = price
    #             continue
    #         profit: int = price - p_min
    #         if profit > max_profit:
    #             max_profit = profit
    #
    #     return max_profit


    # # my attempt to recreate my friend's very different algo
    # def maxProfit(self, prices: list[int]) -> int:
    #     if len(prices) < 2:
    #         return 0
    #     if len(prices) == 2:
    #         profit = prices[1] - prices[0]
    #         return profit if profit >= 0 else 0
    #
    #     yester_price: int = prices[1]
    #     yester_profit: int = prices[1] - prices[0]
    #     max_profit: int = yester_profit
    #
    #     for price in prices[2:]:
    #         today_profit: int = price - yester_price
    #         hodl_profit: int = yester_profit + today_profit
    #         better_profit: int = max(hodl_profit, today_profit)
    #         max_profit = max(max_profit, better_profit)
    #         yester_profit = better_profit
    #         yester_price = price
    #
    #     return max_profit if max_profit >= 0 else 0
