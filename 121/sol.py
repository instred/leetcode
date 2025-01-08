from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i, j = 0, 1
        while j < len(prices):
            buy = prices[i]
            sell = prices[j]
            if buy < sell:
                profit = max(profit, sell-buy)
            else:
                i = j
            j += 1

        return profit
            

if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]  
    prices2 = [7,6,4,3,1]
    print(sol.maxProfit(prices))
    print(sol.maxProfit(prices2))