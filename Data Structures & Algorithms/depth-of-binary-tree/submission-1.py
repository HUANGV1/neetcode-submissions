# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        depth=0

        q=collections.deque()
        
        q.append(root)

        while q:
            for _ in range(len(q)):
                item=q.popleft()
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            depth+=1

        return depth