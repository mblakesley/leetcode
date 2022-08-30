class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # min has to be the first value seen, rather than 0
        p_min: int = prices[0]
        max_profit: int = 0

        for price in prices:
            if price < p_min:
                p_min = price
                continue
            profit: int = price - p_min
            if profit > max_profit:
                max_profit = profit

        return max_profit
