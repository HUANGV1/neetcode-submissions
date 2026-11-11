class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list=collections.defaultdict(list)

        for u,v,t in times:
            adj_list[u].append((v,t))

        minheap=[]

        minheap.append((0,k))

        t=0

        seen=set()

        while minheap:
            w, n1 = heapq.heappop(minheap)

            if n1 in seen: continue

            seen.add(n1)

            t=max(t, w)

            for node, weight in adj_list[n1]:
                if node not in seen:
                    heapq.heappush(minheap, (w+weight, node))

        return t if len(seen)==n else -1
