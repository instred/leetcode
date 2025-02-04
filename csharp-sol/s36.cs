namespace csharp_sol 
{
    public static class S36 
    {

        public static bool CheckRow(int r, int c, int num, char[][] board)
        {
            for (int i = 0; i < 9; i++)
            {
                if (i == c)
                {
                    continue;
                }    
                if (board[r][i] - '0' == num)
                {
                    return true;
                }
            }
            return false;
        }
        
        public static bool CheckCol(int r, int c, int num, char[][] board)
        {
            for (int i = 0; i < 9; i++)
            {
                if (i == r)
                {
                    continue;
                }    
                if (board[i][c] - '0' == num)
                {
                    return true;
                }
            }
            return false;
        }

        public static bool CheckBox(int box_r, int box_c, int num, char[][] board, int r, int c)
        {
            // Console.WriteLine(num);
            for (int i = box_r*3; i < box_r*3+3; i++)
            {
                for (int j = box_c*3; j < box_c*3+3; j++)
                {
                    if (i == r && j == c)
                    {
                        continue;
                    }
                    // Console.WriteLine($"{i}, {j}");
                    if (board[i][j] - '0' == num)
                    {
                        return true;
                    }
                }
            }


            return false;
        }
        public static bool IsValidSudoku(char[][] board) 
        {
            int curr;
            for (int i = 0; i < 9; i++)
            {
                for (int j = 0; j < 9; j++)
                {
                    if (board[i][j] != '.')
                    {
                        curr = board[i][j] - '0';
                        if (CheckRow(i, j, curr, board) || CheckCol(i, j, curr, board) || CheckBox(i/3, j/3, curr, board, i, j))
                        {
                            return false;
                        }
                        
                    }
                }

            }
            
            return true;
        }
    }
}