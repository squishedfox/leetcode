public class Solution {
    // see https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/?envType=study-plan-v2&envId=top-interview-150
    public int MaxProfit(int[] prices) {
        var buy = 0;
        var sell = 1;
        var profit = 0;
        while (sell < prices.Length)
        {
            var calculatedProfit = prices[sell] - prices[buy];
            if (calculatedProfit <= 0)
            {
                while (buy < sell)
                {
                    buy++;
                }
            }
            else if (calculatedProfit > profit)
            {
                profit = calculatedProfit;
            }
            sell++;
        }

        return profit;
    }
}
