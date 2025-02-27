namespace csharp_sol 
{
    public static class S3151 
    {
        public static bool IsArraySpecial(int[] nums) 
        {
            int i = 0;
            int j = 1;
            while (j < nums.Length)
            {
                if ((nums[i] + nums[j]) % 2 == 0)
                {
                    return false;
                }
                i++;
                j++;
            }
            return true;
            
        }
    }
}