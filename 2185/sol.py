from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for w in words:
            m = len(pref)
            if m > len(w):
                continue
            if w[:m] == pref:
                ans += 1
                    

        return ans
            


if __name__ == "__main__":
    sol = Solution()
    words = ["pay","attention","practice","attend"]
    pref = "at"
    words2 = ["leetcode","win","loops","success"]  
    pref2 = "code"
    print(sol.prefixCount(words, pref))
    print(sol.prefixCount(words2, pref2))