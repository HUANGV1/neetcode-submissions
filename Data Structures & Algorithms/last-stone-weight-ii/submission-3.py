class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        '''

        (total-sub)-sub

        dp[i]=can sum be made with i stones (boolean)

        i goes from 0 to half of the sum (best case is both halves equal eachother and difference is 0)

        '''

        dp=[False]*((sum(stones)//2)+1)

        dp[0]=True

        # stone only used once thus go backwards through sums

        
        for i in range(len(stones)):
            for s in range(sum(stones)//2, stones[i]-1, -1):
                dp[s]=dp[s] or dp[s-stones[i]]

        for j in range(sum(stones)//2, -1, -1):
            if dp[j]: return (sum(stones))-(2*j)