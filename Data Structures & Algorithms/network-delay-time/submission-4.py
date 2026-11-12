class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # build adjacency list

        adj_list=collections.defaultdict(list)

        for u,v,t in times:
            adj_list[u].append((v,t))

        heap=[]
        seen=set()

        heapq.heappush(heap,(0,k))
        

        t=0

        while heap:
            w1, n1=heapq.heappop(heap)
            
            if n1 in seen: continue

            seen.add(n1)

            t=max(t, w1)

            for n2, w2 in adj_list[n1]:
                if n2 not in seen: heapq.heappush(heap, (w1+w2,n2))

        return t if len(seen)==n else -1
            
            
