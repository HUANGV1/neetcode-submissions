class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp[i] represents number of ways to create sum i (minimal)
        dp[i+1]=1+dp[i] if one coin can be added to i to create i+1
        
        since this is combinations -> options on the outside (coins)
        since each coin can be used unlimited times -> iterate inner loop forward
        """

        dp=[amount+1]*(amount+1)

        dp[0]=0 # one way to make zero (pick nothing)

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i]=min(dp[i], 1+dp[i-coin])

        return dp[-1] if dp[-1]!=amount+1 else -1