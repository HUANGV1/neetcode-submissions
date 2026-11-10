class Solution:
    def numSquares(self, n: int) -> int:
        
        '''
        options=[1, 2, 3, 4, 5, 6, 7, ...] -> square them
        options are up until floor(root(n))

        define dp:
        dp[i] represents min ways to create i with perfect squares


        '''

        dp=[float('inf')]*(n+1)

        dp[0]=0

        upper=int(n**0.5)

        for option in range(1, upper+1):
            square=option**2
            for s in range(square, n+1):
                dp[s]=min(dp[s], 1+dp[s-square])

        return dp[n]