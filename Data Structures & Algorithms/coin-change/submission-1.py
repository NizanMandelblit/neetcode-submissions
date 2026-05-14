class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[a] = minimum coins needed to make amount a
        dp = [amount+1] * (amount+1)    # init with max value, we want to return dp[amount]
        dp[0] = 0   # (0 coins to make amount 0)

        for a in range(1,amount+1):
            for c in coins:
                if a-c >=0:
                    dp[a] = min(dp[a],1 + dp[a-c])  # 1 symbolize the coin selected
        
        return dp[amount] if dp[amount]!=(amount+1) else -1
