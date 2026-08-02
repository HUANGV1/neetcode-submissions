class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen={}

        for index, num in enumerate(nums):
            missing = target - nums[index]

            if missing in seen:
                return [seen[missing], index]
            
            seen[num] = index


