class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        '''
        [3,4,5,6,1,2]
                 l  
                 r
        [4,5,0,1,2,3]
           r
         l
        '''

        l,r=0,len(nums)-1

        while l<r:

            mid=(l+r)//2

            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
            
        return nums[l]


        

        