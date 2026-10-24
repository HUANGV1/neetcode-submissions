"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque

        if node is None:
            return None

        q=deque()
        clones={}

        q.append(node)

        while q:
            curr_node=q.popleft()
            
            if curr_node not in clones:
                clones[curr_node]=Node(curr_node.val)

            for n in curr_node.neighbors:
                if n not in clones:
                    clones[n]=Node(n.val)
                    q.append(n)
                clones[curr_node].neighbors.append(clones[n])
            
            

        return clones[node]
        
