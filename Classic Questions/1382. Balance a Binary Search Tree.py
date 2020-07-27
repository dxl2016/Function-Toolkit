# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root: return root
        ans = []
        def dfs(root):
            if not root: 
                return
            dfs(root.left)
            ans.append(root)
            dfs(root.right)
        
        def divide(nodes):
            if not nodes:
                return None
            mid = len(nodes)//2 
            nodes[mid].left = divide(nodes[:mid])
            nodes[mid].right = divide(nodes[mid+1:])
            return nodes[mid]
        
        dfs(root)
        return divide(ans)

