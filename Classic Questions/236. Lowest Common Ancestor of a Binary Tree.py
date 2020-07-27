# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node:
                if (node == p or node == q):
                    return node
                
                left_LCA = dfs(node.left)
                right_LCA = dfs(node.right)
               
                if (left_LCA and right_LCA):
                    return node
                
                return (left_LCA or right_LCA)
                    
        if not root or not p or not q:
            return
        return dfs(root)

