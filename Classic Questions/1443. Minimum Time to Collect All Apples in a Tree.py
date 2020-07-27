class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if not edges:
            return 0
        
        def dfs(node):
            it_has_apple = hasApple[node]
            visited.add(node)
            if temp[node]:
                for neigh in temp[node]:
                    if neigh not in visited:
                        it_has_apple |= dfs(neigh)
            
            if it_has_apple and node > 0:
                self.ans += 2
            
            return it_has_apple
        
        visited = set()
        self.ans = 0
        temp = collections.defaultdict(list)
        for items in edges:
            temp[items[0]].append(items[1])
            temp[items[1]].append(items[0])
        
        dfs(0)
        return self.ans
    
    
