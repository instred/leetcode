from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for w in strs:
            w = f"{len(w)}#{w}"
            encoded += w
        return encoded
        
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            
            j = i
            while s[j] != '#':
                j += 1
            leng = int(s[i:j])
            decoded.append(s[j+1: j+1+leng])

            i = j+1+leng

            
        return decoded



if __name__ == "__main__":
    input = ["neet","code","love","you"]
    input2 = ["we","say",":","yes"]    
    s = Solution()
    print(z := s.encode(input))
    print(s.decode(z))
    print(z2 := s.encode(input2))
    print(s.decode(z2))