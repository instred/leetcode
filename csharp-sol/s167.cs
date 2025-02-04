namespace csharp_sol 
{
    public static class S167 
    {
        public static int[] TwoSum(int[] numbers, int target) 
        {
            int l = 0;
            int r = numbers.Length-1;
            int sum;
            while (l < r)
            {
                sum = numbers[l] + numbers[r];
                if (sum < target)
                {
                    l++;
                }
                else if (sum > target)
                {
                    r--;
                }
                else
                {
                    return [l+1, r+1];
                }
            }

            return [];

        }
    }
}
