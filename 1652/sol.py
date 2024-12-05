from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        
        rev = False
        if k < 0:
            code.reverse()
            rev = True
            k = -k

        s = 0
        for i in range(1, k + 1):
            s += code[i]
        res[0] = s
        j=k
        for i in range(1, n):
            j = (j+1)%n
            res[i] = res[i-1] - code[i] + code[j]

        if rev:
            res.reverse()
            return res
        else:
            return res

if __name__ == "__main__":
    s = Solution()
    code = [5,7,1,4]
    k = 3
    code2 = [1,2,3,4]
    k2 = 0
    code3 = [2,4,9,3]
    k3 = -2
    print(s.decrypt(code, k))
    print(s.decrypt(code2, k2))
    print(s.decrypt(code3, k3))