from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        numToIdx = { num : i for i, num in enumerate(arr) }
        
        min_idx = float('inf')

        r, c = len(mat), len(mat[0])

        for i in range(r):
            max_row_idx = float('-inf')

            for j in range(c):
                curr_idx = numToIdx[mat[i][j]]
                max_row_idx = max(max_row_idx, curr_idx)

            min_idx = min(max_row_idx, min_idx)

        for j in range(c):
            max_row_idx = float('-inf')

            for i in range(r):
                curr_idx = numToIdx[mat[i][j]]
                max_row_idx = max(max_row_idx, curr_idx)

            min_idx = min(max_row_idx, min_idx)

        return min_idx

        




if __name__ == "__main__":
    sol = Solution()
    arr = [1,4,5,2,6,3]
    mat = [[4,3,5],[1,2,6]]  
    arr2 = [2,8,7,4,1,3,5,6,9]  
    mat2 = [[3,2,5],[1,4,6],[8,7,9]]
    print(sol.firstCompleteIndex(arr, mat))
    print(sol.firstCompleteIndex(arr2, mat2))
