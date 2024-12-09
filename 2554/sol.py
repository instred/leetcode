from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        curr_sum = 0
        banned = set(banned)
        ans = 0
        for i in range(1, n+1):
            if i not in banned and curr_sum+i <= maxSum:
                curr_sum += i
                ans += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    banned = [1,6,5]
    n = 5
    maxSum = 6
    banned2 = [1,2,3,4,5,6,7]
    n2 = 8
    maxSum2 = 1
    banned3 = [11]
    n3 = 7
    maxSum3 = 50
    print(s.maxCount(banned, n, maxSum))
    print(s.maxCount(banned2, n2, maxSum2))
    print(s.maxCount(banned3, n3, maxSum3))