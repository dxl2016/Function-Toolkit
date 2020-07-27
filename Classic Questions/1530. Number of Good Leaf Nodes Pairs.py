# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = collections.defaultdict(list)
        leaf = []
        
        def dfs(node, par = None):
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)
                
                if node and not node.left and not node.right:
                    leaf.append(node)

        dfs(root)
        # print(graph)
        # print(leaf)
   
        ans = 0
        for i in leaf:
            q = [(i,0)]
            seen = set()
            
            while(q):
                node, c = q.pop(0)
                if c > distance:
                    break
                
                if node:
                    seen.add(node)
                    for neigh in graph[node]:
                        if neigh not in seen:
                            q.append((neigh, c+1))
                    
                    if node != i and node in leaf and c <= distance:
                        ans += 1
                    
        return ans//2

