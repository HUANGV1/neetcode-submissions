class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        [1][2][3][4][5][6][7]
        
        when at current house, choose the max of:
        1. not robbing this house; take the max of the house before
        2. rob this house; disregard the previous house, add current house to previous max

        currmax
        house1, house2

        take/skip DP

        '''
        if len(nums)==1:
            return nums[0]


        dp=[0 for i in range(len(nums))]

        dp[0]=nums[0]
        dp[1]=max(nums[0], nums[1])

        for i in range(2, len(nums)):
            skip=dp[i-1]
            take=dp[i-2]+nums[i]

            dp[i] = max(skip, take)

        return dp[-1]