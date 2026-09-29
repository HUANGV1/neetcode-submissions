class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import defaultdict

        seen=defaultdict(int)

        for num in nums:
            seen[num]+=1

        freq=[]
        for i in range(len(nums)+1):
            freq.append([])
        # now, each index freq[i] is a list of the numbers which repeate i times

        for num, count in seen.items():
            freq[count].append(num)

        ret=[]
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                ret.append(num)
                if len(ret)==k:
                    return ret

