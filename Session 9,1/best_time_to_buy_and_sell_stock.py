from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        to_buy = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - to_buy)
            to_buy = min(to_buy, prices[i])

        return max_profit
