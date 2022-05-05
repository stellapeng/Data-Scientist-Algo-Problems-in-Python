# a variant of dijkstra: dist_to_next_node is the maximum absolute difference
# dist_to[x][y] recordes the maximum absolute difference from (0, 0) ro (x, y)

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
            
            for n in self.neighbors(heights, cur_x, cur_y):
                if n:
                    next_node_id = n[0]
                    dist_to_next_node = dist_to[cur_node_id] + n[1]

                    if (dist_to[next_node_id] > dist_to_next_node):
                        dist_to[next_node_id] = dist_to_next_node
                        heapq.heappush(pq, (dist_to_next_node, next_node_id))
        return dist_to
    
    def neighbors(self, heights, x, y):
        m, n = len(heights), len(heights[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for d in dirs:
            nx = x + d[0]
            ny = y + d[1]
            if (nx <0 or nx>= m or ny<0 or ny>=n):
                continue
            neighbors.append((nx, ny))
        return neighbors
    
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        dist_to = [[float('inf') for i in range(n)] for i in range(m)]
        dist_to[0][0] = 0
        pq = []
        heapq.heappush(pq, (0, 0, 0))
        
        while(pq):
            cur_state = heapq.heappop(pq)
            cur_x = cur_state[1]
            cur_y = cur_state[2]
            cur_dist_from_start = cur_state[0]
            
            if (cur_x == (m - 1) and cur_y == (n - 1)):
                return cur_dist_from_start
            
            if (cur_dist_from_start > dist_to[cur_x][cur_y]):
                continue
            
            for neignbour in self.neighbors(heights, cur_x, cur_y):
                next_x = neignbour[0]
                next_y = neignbour[1]
                dist_to_next_node = max(dist_to[cur_x][cur_y], 
                        abs(heights[cur_x][cur_y]-heights[next_x][next_y]))

                if (dist_to[next_x][next_y] > dist_to_next_node):
                    dist_to[next_x][next_y] = dist_to_next_node
                    heapq.heappush(pq, (dist_to_next_node, next_x, next_y))
            
        return -1
        