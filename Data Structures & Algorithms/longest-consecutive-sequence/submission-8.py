class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nums=list(set(nums))

        nums.sort()

        step=[]

        for i in range(1, len(nums)):
            step.append(nums[i]-nums[i-1])

        longest=0
        length=0

        for i in range(len(step)):
            if step[i]==1:
                length+=1
            else:
                longest=max(longest, length+1)
                length=0

        longest=max(longest, length+1)
        
        return longest



        """

        [2,20,4,10,3,4,5]
        [2,3,4,4,5,10,20]
        [2,1,1,0,1,5,10]

        [2,3,4,5,10,20]
        [2,1,1,1,5,10]

        [0,3,2,5,4,6,1,1]
        [0,1,1,2,3,4,5,6]
        [0,1,0,1,1,1,1]

        """