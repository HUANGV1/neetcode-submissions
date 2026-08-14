class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_prod=1
        suffix_prod=1
        i=1
        while i<len(nums):
            suffix_prod*=nums[i]
            i+=1

        ret=[]

        ret.append(suffix_prod)

        i=1

        while i<(len(nums)-1):
            if nums[i]==0:
                suffix_prod=1
                j=i+1
                while j<len(nums):
                    suffix_prod*=nums[j]
                    j+=1
            else:
                suffix_prod/=nums[i]

            prefix_prod*=nums[i-1]

            ret.append(int(prefix_prod*suffix_prod))

            i+=1

        prefix_prod*=nums[-2]
        ret.append(prefix_prod)

        return ret
            