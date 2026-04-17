class Solution {
   public:
    int maxProfit(vector<int>& prices) {
        // brute force o(n^2)
        //     int profit = 0;
        //     for (int i = 0; i < prices.size(); i++) {
        //         for (int j = i+1; j < prices.size(); j++) {
        //             profit = max(profit, prices[j] - prices[i]);
        //         }
        //     }
        //     return profit;

        // two pointers
        int l = 0;
        int r = 1;
        int profit = 0;
        while (r < prices.size()) {
            if (prices[l] < prices[r])
                profit = max(profit, prices[r] - prices[l]);
            else if (prices[l] > prices[r])
                l = r;
            r += 1;
        }
        return profit;
    }
};
