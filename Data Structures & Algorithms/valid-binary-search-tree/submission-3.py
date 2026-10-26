# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_valid(min_val, node, max_val):

            if not node: return True
            
            if not node.val>min_val or not node.val<max_val:
                return False

            return is_valid(min_val, node.left, node.val) and is_valid(node.val, node.right, max_val)

        return is_valid(float('-inf'), root, float('inf'))