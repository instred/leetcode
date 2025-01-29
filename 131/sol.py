from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        part = []

        def backtrack(i):
            if i == len(s):
                ans.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i : j+1])
                    backtrack(j+1)
                    part.pop()    


        backtrack(0)

        return ans
    
    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    

class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        part = []

        def backtrack(i, curr):
            if curr == len(s):
                ans.append(part.copy())
                return

            curr += 1
            if part:
                part[-1] += s[i]
                backtrack(i+1, curr)
                part[-1] = part[-1][:-1] 
            part.append(s[i])
            backtrack(i+1, curr)
            part.pop()    
            curr -= 1

        backtrack(0, 0)
        ans_filtered = []
        for p in ans:
            for sub in p:
                if not self.isPalindrome(sub):
                    break
            else:
                ans_filtered.append(p) 

        return ans_filtered

    def isPalindrome(self, substring: List[str]) -> bool:
        l, r = 0, len(substring)-1
        while l < r:
            if substring[l] != substring[r]:
                return False
            l += 1
            r -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    s = "aab"
    s2 = "a"
    print(sol.partition(s))
    print(sol.partition(s2))