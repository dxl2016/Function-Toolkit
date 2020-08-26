# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def dfs(node, tot):
            if not node:
                return 0
            l = dfs(node.left, tot)
            r = dfs(node.right, tot)
            self.ans = max(self.ans, l*(tot-l), r*(tot-r))
            return l+r+node.val
        
        self.ans = 0
        tot = dfs(root, 0)
        dfs(root, tot)
        return self.ans % (10**9+7)

