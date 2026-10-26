# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        old idea: dfs through the bst and for each node keep track of what came before it (maybe use dictionary)
        once found both target nodes, compare their lists of ancestors (starting from end of list)
        
        new way:
        compare the current node with p and q
        if p and q are both greater, then go to the right of the current node
        if p and q are both less, then go to the left of the current node
        if p and q are on oppoiste sides or one of them is the node, then LCA = current node

        '''

        node=root

        while node:
            if p.val>node.val and q.val>node.val:
                node=node.right
            elif p.val<node.val and q.val<node.val:
                node=node.left
            else:
                return node

