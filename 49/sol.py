from typing import List
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = {}
        for s in strs:
            a = ''.join(sorted(s))
            if a in grps:
                grps[a].append(s)
            else:
                grps[a] = [s]
        return (list(grps.values()))
            

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    strs2 = [""]
    strs3 = ["a"]
    s = Solution()
    print(s.groupAnagrams(strs))
    print(s.groupAnagrams(strs2))
    print(s.groupAnagrams(strs3))