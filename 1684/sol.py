from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            isin = True
            for ch in word:
                if ch not in allowed:
                    isin = False
            if isin == True:
                ans += 1 
        return ans
    

if __name__ == "__main__":

    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    allowed2 = "abc"
    words2 = ["a","b","c","ab","ac","bc","abc"]
    allowed3 = "cad"
    words3 = ["cc","acd","b","ba","bac","bad","ac","d"]
    s = Solution()
    print(s.countConsistentStrings(allowed, words))
    print(s.countConsistentStrings(allowed2, words2))
    print(s.countConsistentStrings(allowed3, words3))




    
