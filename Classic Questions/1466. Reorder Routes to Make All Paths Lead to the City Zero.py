class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = []
        valid_roads = set()
        for i in range(n):
            graph.append([])
        for i,j in connections:
            graph[i] += [j]
            graph[j] += [i]
            valid_roads.add( (i,j) )
            
        self.ans = 0
        # not_valid_roads = set()
        visited = [False]*n
        
        def dfs(node, target):
            visited[node] = True
            if target in graph[node] and (node, target) not in valid_roads:
                self.ans += 1
                # not_valid_roads.add( (node, target) )
            for x in graph[node]:
                if not visited[x]:
                    dfs(x, node)
        
        visited[0] = True    
        for node in range(n):
            # start with nodes connected to target node_0
            if not visited[node] and node in graph[0]:
                dfs(node, 0)

        return self.ans

