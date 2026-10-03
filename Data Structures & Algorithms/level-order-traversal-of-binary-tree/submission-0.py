# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque

        q=deque()
        q.append(root)
        ret=[]

        while q:
            length=len(q)
            level=[]

            for _ in range(length):
                el=q.popleft()
                if el:
                    q.append(el.left)
                    q.append(el.right)
                    level.append(el.val)
            if level:
                ret.append(level)

        return ret