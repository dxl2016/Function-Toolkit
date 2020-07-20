class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        temp = []
        for x in range(0, numCourses):
            temp.append([])
        for i,j in prerequisites:
            temp[i] += [j]

        for x in range(0, numCourses):
            stack = [x]
            visited = set()
            while(stack):
                curr_node = stack.pop()
                if visited and curr_node == x:
                    return False
                if curr_node not in visited: 
                    visited.add(curr_node)
                    stack += temp[curr_node]
        return True

