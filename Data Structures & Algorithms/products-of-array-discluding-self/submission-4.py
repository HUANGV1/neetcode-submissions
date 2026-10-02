class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix=[]
        for i in range(len(nums)):
            if i==0:
                prefix.append(1)
            else:
                prefix.append(nums[i-1]*prefix[i-1])

        suffix=[]
        for i in range(len(nums)-1, -1, -1):
            if i==len(nums)-1:
                suffix.append(1)
            else:
                suffix.append(nums[i+1]*suffix[-1])

        ret=[]
        suffix.reverse()
        for i in range(len(prefix)):
            ret.append(prefix[i]*suffix[i])

        return ret


"""

1,2,4,6

1,1,2,8
*
1,6,24,48

"""