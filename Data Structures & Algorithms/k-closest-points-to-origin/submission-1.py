class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxheap=[]

        for x,y in points:
            heapq.heappush(maxheap, (-(x**2 + y**2),[x,y]))
            if len(maxheap)>k:
                heapq.heappop(maxheap)

        ret=[]

        return [loc for val, loc in maxheap]