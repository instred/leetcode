namespace csharp_sol 
{
    public static class S3105 
    {
        public static int LongestMonotonicSubarray(int[] nums)
        {
            int res = 1;
            int lenInc = 1, lenDec = 1;
            for (int i = 0; i < nums.Length-1; i++)
            {
                if (nums[i] > nums[i+1])
                {
                    lenDec++;
                    lenInc = 1;
                }
                else if (nums[i] < nums[i+1])
                {
                    lenInc++;
                    lenDec = 1;
                }
                else
                {
                    lenInc = 1;
                    lenDec = 1;
                }
                
            res = Math.Max(res, Math.Max(lenDec, lenInc));
            }


            return res;
        }

    }
}
