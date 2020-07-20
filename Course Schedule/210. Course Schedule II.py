class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(i):
            visited[i] = 1
            if i in tmp:
                for j in tmp[i]:
                    if visited[j] == 1:
                        return False
                    elif visited[j] == 0:
                        if not dfs(j):
                            return False
            q.appendleft(i)
            visited[i] = 2
            return True
                                  
        tmp = collections.defaultdict(list)
        for items in prerequisites:
            if items[1] not in tmp:
                tmp[items[1]] = [items[0]]
            else:
                tmp[items[1]] += [items[0]]
        

        visited = [0]*numCourses
        q = deque()
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        return list(q)

