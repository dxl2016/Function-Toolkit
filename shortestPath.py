def shortestPath(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for p, (i,j) in enumerate(edges):
            graph[i].append([succProb[p],j])
            graph[j].append([succProb[p],i])

        dist = collections.defaultdict(int)
        dist[start] = -1
        pq = [[-1,start]]

        while(pq):
            curr_dist, curr_node = heapq.heappop(pq)
            for neigh_dist, neighbor in graph[curr_node]:
                curr_prob = curr_dist*neigh_dist
                if curr_prob < dist[neighbor]:
                    heapq.heappush(pq, [curr_prob,neighbor])
                    dist[neighbor] = curr_prob


        return -dist[end]
