class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total=sum(stones)

        half=total//2


        '''
        dp[i] represents "can sum i be made with a subset of stones"
        '''
        dp=[False]*(half+1)

        dp[0]=True

        '''
        bounded knapsack (0/1) - thus backwards through dp
        '''

        for i in range(len(stones)):
            for s in range(half, stones[i]-1, -1): # why does this end at stones[i]
                dp[s]=dp[s] or dp[s-stones[i]]

        

        for j in range(half, -1, -1):
            if dp[j]: return (total-j)-j