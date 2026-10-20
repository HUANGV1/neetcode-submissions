class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]

        
        def rob_range(start, end):
            dp=[0]*(end-start+1)

            dp[0]=nums[start]

            if start == end:
                return dp[0]

            dp[1]=max(nums[start], nums[start+1])

            for i in range(2, len(dp)):
                skip=dp[i-1]
                take=dp[i-2]+nums[start+i]

                dp[i]=max(skip, take)

            return dp[-1]

        no_first=rob_range(0, len(nums)-2)
        no_last=rob_range(1, len(nums)-1)

        return max(no_first, no_last)