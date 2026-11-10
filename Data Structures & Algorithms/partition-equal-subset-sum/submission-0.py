class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        half=sum(nums)

        if half%2!=0: return False

        goal=half//2

        '''
        from 0 to goal, are we able to find a subset to make that number
        iterate from 0 to goal, then iterate through nums (backwards) to see if we can use that to make subset?
        '''

        dp=[False]*(goal+1)
        dp[0]=True

        for num in nums:
            for i in range(goal, num-1, -1):
                dp[i]=dp[i] or dp[i-num]

        return dp[-1]
