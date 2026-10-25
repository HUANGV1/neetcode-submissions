class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        import heapq

        freq=collections.defaultdict(int)

        for num in nums:
            freq[num]+=1

        heap=[]

        for key in freq:
            heapq.heappush(heap, (freq[key], key))

            if len(heap)>k:
                heapq.heappop(heap)
        
        out=[]

        for freqs, num in heap:
            out.append(num)

        return out

