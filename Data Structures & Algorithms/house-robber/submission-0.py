class Solution:
    def rob(self, nums: List[int]) -> int:
        # we set these to 0 
        rob1,rob2=0,0

        # [rob1, rob2, n, n+1]

        for n in nums:
            # find max of either robbing n or not robbing not
            # n+rob1 means robbing n, and we get the max of the house 2 pos before, or we don't rob n and just take rob2
            temp=max(n+rob1, rob2)
            
            # increment to n+1. now we will move rob1, rob2 right
            rob1=rob2
            rob2=temp

        return rob2 # the max
