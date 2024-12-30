from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        return a == b
    

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = {}, {}
        
        for ch in s:
            a[ch] = a.get(ch, 0) + 1
        
        for ch in t:
            b[ch] = b.get(ch, 0) + 1

        return a == b
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    s2 = "rat"
    t2 = "car"
    ss = Solution2()
    print(ss.isAnagram(s, t))
    print(ss.isAnagram(s2, t2))