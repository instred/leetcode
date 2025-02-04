namespace csharp_sol 
{
    public static class S238 
    {
        public static int[] ProductExceptSelf(int[] nums) 
        {
            int n = nums.Length;
            int[] ans = new int[n];
            int start = 1;

            for (int i = 0; i < n; i++)
            {
                ans[i] = start;
                start *= nums[i];
            }
            start = 1;
            for (int i = n-1; i > -1 ; i--)
            {
                ans[i] *= start;
                start *= nums[i];
            }
            return ans;


        }
    }
}