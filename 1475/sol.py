
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []

        for i in range(len(prices)):
            curr_price = prices[i]
            dc = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= curr_price:
                    dc = prices[j]
                    break
            ans.append(curr_price-dc)
        return ans
    
class Solution2:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        result = prices[:]
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                print(stack, i, result)
                idx = stack.pop()
                result[idx] = prices[idx] - prices[i]
            stack.append(i)
        return result
            


if __name__ == "__main__":
    prices = [8,4,6,2,3]
    prices2 = [1,2,3,4,5]
    prices3 = [10,1,1,6]
    s = Solution2()
    print(s.finalPrices(prices))
    print(s.finalPrices(prices2))
    print(s.finalPrices(prices3))