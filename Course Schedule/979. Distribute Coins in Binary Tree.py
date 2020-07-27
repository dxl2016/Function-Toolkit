# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(node):
            if node is None:
                return 0
            
            l_ans = dfs(node.left)
            r_ans = dfs(node.right)
            
            self.ans += abs(l_ans)+abs(r_ans)
            return node.val+l_ans+r_ans-1
                 
        dfs(root)
        return self.ans

