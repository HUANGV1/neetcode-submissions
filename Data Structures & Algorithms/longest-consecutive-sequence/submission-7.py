class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset=set(nums)

        longest=0

        for num in numset:
            if num-1 not in numset: #this is the beginning of a potential series
                length=1
                while num+length in numset:
                    length+=1
                longest=max(longest, length)
                length=0
        
        return longest