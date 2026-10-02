class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset=set(nums)

        longest=0
        length=0

        for num in numset:
            if num-1 not in numset:
                length+=1
                while True:
                    if num+length not in numset:
                        longest=max(longest, length)
                        length=0
                        break
                    length+=1
        return longest
            


            # [1,2,3,4,10,20]