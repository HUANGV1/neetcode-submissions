class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ret=[1]*len(nums) # [1, 1, 1, ...]

        prefix=1

        # left to right. calc all prefix. each ret[i] represents product of nums before
        for i in range(len(nums)):
            ret[i]=prefix
            prefix*=nums[i] # multiply next num

        postfix=1

        # go right to left, calc the postfix from nums and then multiply to respective ret[i]
        for i in range(len(nums)-1, -1, -1):
            ret[i]*=postfix
            postfix*=nums[i]

        return ret