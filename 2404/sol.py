from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
    
        occurences = {}
        for n in nums:
            if n % 2 == 0:
                occurences[n] = occurences.get(n, 0) + 1

        ans = -1
        c = 0
        for k, v in occurences.items():
            if v > c or v == c and k < ans:
                ans = k
                c = v

        return ans 
