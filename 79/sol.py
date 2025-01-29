from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.n = len(board)
        self.m = len(board[0])
        visited = [[False] * self.m for _ in range(self.n)]

        def dfs(startx, starty, curr_char):
                
                if curr_char == len(word):
                    return True
                
                if startx < 0 or starty < 0 or startx >= self.m or starty >= self.n or word[curr_char] != board[starty][startx] or visited[starty][startx]:
                    return False
                            

                visited[starty][startx] = True
                
                res = (dfs(startx+1, starty, curr_char+1) or \
                    dfs(startx-1, starty, curr_char+1) or \
                    dfs(startx, starty+1, curr_char+1) or \
                    dfs(startx, starty-1, curr_char+1))
                visited[starty][startx] = False                
                return res
        
        for i in range(self.n):
            for j in range(self.m):
                
                if dfs(j, i, 0): return True
    
        return False
    
        

if __name__ == "__main__":

    sol = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]  
    wordd = "ABCCED"  
    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]  
    wordd2 = "SEE"  
    board3 = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    wordd3 = "ABCESEEEFS"
    # print(sol.exist(board, wordd))
    # print(sol.exist(board2, wordd2))
    print(sol.exist(board3, wordd3))