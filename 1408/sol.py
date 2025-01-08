from typing import List

class Solution2:
    def stringMatching(self, words: List[str]) -> List[str]:
        w_set = set(words)
        ans = set()
        for w in words:
            for ws in w_set:
                if w == ws:
                    continue
                if w in ws:
                    ans.add(w)

        return list(ans)

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        w = ' '.join(words)
        s = [i for i in words if w.count(i) > 1]
        return s


if __name__ == "__main__":
    sol = Solution()
    words = ["mass","as","hero","superhero"]  
    words2 = ["leetcode","et","code"]  
    words3 = ["blue","green","bu"]
    print(sol.stringMatching(words))
    print(sol.stringMatching(words2))
    print(sol.stringMatching(words3))