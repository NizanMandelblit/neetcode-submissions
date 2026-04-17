class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force O(n^2)
        # res = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         res = max(res, prices[j]- prices[i])

        # return res

        # two pointers O(n)
        res = 0 
        buy, sell, = 0, 1
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                res = max(res, prices[sell]-prices[buy])
            elif prices[buy] > prices[sell]:
                buy=sell
            sell+=1
        return res