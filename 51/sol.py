from typing import List

class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ans = []
        board = [["."] * n for _ in range(n)]

        def dfs(r):

            if r == n:
                a = ["".join(x) for x in board]
                ans.append(a) 
                return
            
            for c in range(n):
                if self.isSafe(r, c, board):
                    board[r][c] = "Q"
                    dfs(r+1)
                    board[r][c] = "."
        dfs(0)
        return ans

    def isSafe(self, r, c, board):
        row = r-1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        row, col = r-1, c-1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1    
            col -= 1
        row, col = r-1, c+1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1    
            col += 1

        return True
    
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res

            




if __name__ == "__main__":
    sol = Solution()
    nn = 4  
    nn2 = 1
    print(sol.solveNQueens(nn))
    print(sol.solveNQueens(nn2))