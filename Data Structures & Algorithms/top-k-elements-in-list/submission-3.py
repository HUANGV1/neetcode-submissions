class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        import heapq

        seen=defaultdict(int) # (num, freq)

        for num in nums:
            seen[num]+=1

        heap=[]

        for key in seen.keys():
            heapq.heappush(heap, (seen[key], key)) # freq, num because heap will compare first value in tuple
            if len(heap)>k:
                heapq.heappop(heap)

        res=[]

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


        