class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # only count profit if its > 0
        diff = 0

        profit = 0

        for i in range(1,len(prices)):

            diff = prices[i] - prices[i-1]

            if diff > 0:
                profit += diff

        return profit