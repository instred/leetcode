namespace csharp_sol 
{
    public static class S1752 
    {
        public static bool Check(int[] nums) 
        {
            
            int n = nums.Length;
            if (n<=1) return true;

            int count = 0;

            for (int i = 1; i < n; i++)
            {
                if (nums[i] < nums[i-1]) 
                {
                    count++;
                    if (count>1) return false;
                }
            }
            if (nums[0] < nums[n-1])
            {
                count++;
            }
            return count<=1;
        }
    }
}
