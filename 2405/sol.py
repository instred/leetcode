class Solution:
    def partitionString(self, s: str) -> int:
        
        string = set()
        ans = 1

        for ch in s:
            if ch in string:
                string = set({ch})
                ans += 1
            string.add(ch)

        return ans



        




if __name__ == "__main__":
    sol = Solution()
    s = "abacaba"  
    s2 = "ssssss"
    s3 = "hdklqkcssgxlvehva"
    print(sol.partitionString(s))
    print(sol.partitionString(s2))
    print(sol.partitionString(s3))