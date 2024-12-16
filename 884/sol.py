from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        ans = []
        combined = s1.split() + s2.split()
        words = {}

        for w in combined:
            words[w] = words.get(w, 0) + 1

    
        return [w for w in words if words[w] == 1]
                
       





if __name__ == "__main__":
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    s12 = "op vu kux dn jsenj hbdez hbdez nbenh z op dxmqd op"
    s22 = "kux wnx wnx wbi jsenj nlgfn vu f vu fvxas dn op tb"
    s = Solution()
    print(s.uncommonFromSentences(s1, s2))
    print(s.uncommonFromSentences(s12, s22))