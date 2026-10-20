class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp=[amount+1]*(amount+1)


        dp[0]=0

        for subsum in range(1, amount+1):
            for coin in coins:
                if subsum-coin>=0: # possible minimal dp
                    dp[subsum]=min(dp[subsum], 1+dp[subsum-coin])

        return dp[amount] if dp[amount]!=(amount+1) else -1