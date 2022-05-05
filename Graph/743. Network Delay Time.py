import heapq

class Solution:
    def dijkstra(self, k, graph):
        dist_to = [float('inf')] * (len(graph)+1)
        dist_to[k] = 0
        pq = []
        heapq.heappush(pq, (0, k))
        
        while(pq):
            cur_state = heapq.heappop(pq)
            cur_node_id = cur_state[1]
            cur_dist_from_start = cur_state[0]
            
            if (cur_dist_from_start > dist_to[cur_node_id]):
                continue
            
            for n in graph[cur_node_id]:
                if n:
                    next_node_id = n[0]
                    dist_to_next_node = dist_to[cur_node_id] + n[1]

                    if (dist_to[next_node_id] > dist_to_next_node):
                        dist_to[next_node_id] = dist_to_next_node
                        heapq.heappush(pq, (dist_to_next_node, next_node_id))
        return dist_to
        
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for i in range(1, n+1):
            graph[i].append([])
        for e in times:
            graph[e[0]].append([e[1], e[2]])
            
        dist_to = self.dijkstra(k, graph)

        res = 0
        for i in range(1, len(dist_to)):
            if dist_to[i] == float('inf'):
                return -1
            res = max(res, dist_to[i])
        return res