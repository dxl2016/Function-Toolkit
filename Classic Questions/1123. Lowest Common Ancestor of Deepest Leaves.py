# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        graph = collections.defaultdict(list)
        leaves = {}
        check = []
        def dfs(c, node, par=None):
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(c+1, node.left, node)
                dfs(c+1, node.right, node)
                
                if not node.left and not node.right:
                    if c not in leaves:
                        leaves[c] = [node]
                    else:
                        leaves[c] += [node]

        dfs(0, root)

        leaves = sorted(leaves.items(), reverse=True)
        if leaves and len(leaves[0][1]) == 1:
            return leaves[0][1][0]
        
        q = leaves[0][1]
        for items in q:
            check.append(items.val)
        ans = []
        
        def bfs(node):
            if not node:
                return False
            lac = True
            seen.add(node)
            if graph[node]:
                for neigh in graph[node]:
                    if neigh not in seen:
                        lac |= bfs(neigh)
            if lac and node not in q:
                ans.append(node)

            return node in q
            
        seen = set()
        bfs(q[0])
        
        def traverse(node):
            if node:
                if node.val in c:
                    c.remove(node.val)
                traverse(node.left)
                traverse(node.right)
            
        for tree in ans[::-1]:
            c = check
            traverse(tree)
            if not c:
                return tree

