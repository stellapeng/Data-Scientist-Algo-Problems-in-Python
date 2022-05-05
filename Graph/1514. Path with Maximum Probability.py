# dijkstra is also applicable in
# 1. undirected graph
# 2. maximum path problem (finding the maximum is also a problem with optimal structure)

class Solution:
    def dijkstra(self, graph, start, end):
        dist_to = [-1] * (len(graph))
        dist_to[start] = 1
        pq = []

        # the first element is -1 * distance, the reverse of min heap is max heap
        heapq.heappush(pq, (-1, 1, start)) 
        
        while(pq):
            cur_state = heapq.heappop(pq)
            cur_node_id = cur_state[2]
            cur_dist_from_start = cur_state[1]
            
            if cur_node_id == end:
                return cur_dist_from_start
            
            if (cur_dist_from_start < dist_to[cur_node_id]):
                continue
            
            for n in graph[cur_node_id]:
                if n:
                    next_node_id = n[0]
                    dist_to_next_node = dist_to[cur_node_id] * n[1]

                    if (dist_to[next_node_id] < dist_to_next_node):
                        dist_to[next_node_id] = dist_to_next_node
                        heapq.heappush(pq, (-dist_to_next_node, dist_to_next_node, next_node_id))
        return 0
    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = defaultdict(list)
        for i in range(n):
            graph[i] = []
            
        for i in range(len(edges)):
            e = edges[i]
            graph[e[0]].append([e[1], succProb[i]])
            graph[e[1]].append([e[0], succProb[i]])
            
        return self.dijkstra(graph, start, end)
        