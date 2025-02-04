namespace csharp_sol 
{
    public static class S121 
    {
        public static int MaxProfit(int[] prices) 
        {
            int res = 0;
            int l = 0;
            int r = 1;
            while (r < prices.Length)
            {
                int buy = prices[l];
                int sell = prices[r];
                if (buy < sell)
                {
                    res = Math.Max(res, sell-buy);
                }
                else
                {
                    l = r;
                }
                r++;

            }
            return res;
        }
    }
}