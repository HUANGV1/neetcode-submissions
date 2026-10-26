# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ret=[]

        q=collections.deque()

        q.append(root)

        while q:
            sub=[]
            for _ in range(len(q)):
                item = q.popleft()
                
                sub.append(item.val)
            
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
                
            ret.append(sub)

        return ret

        