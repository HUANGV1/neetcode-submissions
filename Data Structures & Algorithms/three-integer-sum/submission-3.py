class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        i+j+k=0
        i=-(j+k)

        [-4,-1,-1,0,1,2]
        

        """

        nums.sort()
        res=[]

        for index, val in enumerate(nums):
            if val>0:
                break

            if index>0 and nums[index]==nums[index-1]:
                continue
            
            # start

            l, r = index+1, len(nums)-1

            while l<r:
                threesum=val+nums[l]+nums[r]

                if threesum<0:
                    l+=1
                elif threesum>0:
                    r-=1
                elif threesum==0:
                    res.append([val, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1    





        return res