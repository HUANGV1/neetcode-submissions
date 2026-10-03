class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r=0,len(nums)-1

        while l<=r:
            mid=(r+l)//2

            if nums[mid]==target:
                return mid


            if nums[mid]>=nums[l]: #left is sorted
                if target>nums[mid] or target<nums[l]: #not in left section
                    l=mid+1
                else: #in left section
                    r=mid-1
            else: #right is sorted
                if target<nums[mid] or target>nums[r]: #not in right section
                    r=mid-1
                else: #in right section
                    l=mid+1
            
        return -1

