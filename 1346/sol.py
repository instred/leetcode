from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] == 0:
                if 0 in arr[i+1:]: return True
                else: continue
            if 2*arr[i] in arr:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    arr = [10,2,5,10]
    arr2 = [3,1,7,11]
    arr3 = [7,1,14,11]
    arr4 = [-20,8,-6,-14,0,-19,14,4]
    # print(s.checkIfExist(arr))
    # print(s.checkIfExist(arr2))
    # print(s.checkIfExist(arr3))
    print(s.checkIfExist(arr4))