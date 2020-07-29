class Solution:
    def countSubTrees(self, n: int, y: List[List[int]], l: str) -> List[int]: 
        def dfs(node, parent):
            counter = collections.Counter()
            counter[l[node]] += 1
            
            for neigh in graph[node]:
                if neigh == parent: 
                    continue
                counter += dfs(neigh, node)
            
            result[node] = counter[l[node]]

            return counter

        graph = [[] for _ in range(n)]
        for (f,t) in y:
            graph[f].append(t)
            graph[t].append(f)
        
        result = [0] * n
        dfs(0, None)
        
        return result

