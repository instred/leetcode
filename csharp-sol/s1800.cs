namespace csharp_sol 
{
    public static class S1800 
    {
        public static int MaxAscendingSum(int[] nums) 
        {
            int res = nums[0];
            int currRes = nums[0];

            for (int i = 0; i < nums.Length-1; i++)
            {
                // Console.WriteLine(currRes);
                if (nums[i] < nums[i+1])
                {
                    currRes += nums[i+1];
                }
                else
                {
                    currRes = nums[i+1];
                }
                res = Math.Max(res, currRes);
            }
            return res;   
        }
    }
}
