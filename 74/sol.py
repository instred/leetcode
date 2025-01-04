from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        xlen, ylen = len(matrix[0]), len(matrix)
        i, j = 0, (xlen*ylen)-1
        while i <= j:
            mid = (i + j) // 2
            x, y = mid % xlen, mid // xlen
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                j = mid - 1
            else:
                i = mid + 1

        return False
    
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]  
    target = 3  
    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]  
    target2 = 13
    print(sol.searchMatrix(matrix, target))
    print(sol.searchMatrix(matrix2, target2))