# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''

        dfs through nodes and for each node, we calcualate the straigt max path down its child (dfs)
        at the same time, see if diverging from current node for both chidlren is the longest.

        '''

        res=[root.val]

        def dfs(root):
            if not root: return 0

            leftMax=max(0, dfs(root.left))
            rightmax=max(0, dfs(root.right))

            res[0]=max(res[0], root.val+leftMax+rightmax)

            return root.val+max(leftMax, rightmax)

        dfs(root)

        return res[0]

            