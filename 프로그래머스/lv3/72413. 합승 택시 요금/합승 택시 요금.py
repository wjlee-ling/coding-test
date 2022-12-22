def solution(n, s, a, b, fares):
    from heapq import heappush, heappop
    from collections import defaultdict
    
    graph = defaultdict(dict)
    for (c,d,f) in fares:
        graph[c].update({d:f})
        graph[d].update({c:f})
    
    def dijkstra(start, destination):
        inf = float('inf')
        distances = [inf] * (n+1)
        distances[start] = 0
        queue = [(distances[start], start)]
        while queue:
            curr_dist, curr = heappop(queue)
            if distances[curr] < curr_dist:
                continue
            for new, new_dist in graph[curr].items():
                dist = new_dist + curr_dist
                if dist < distances[new]:
                    distances[new] = dist
                    heappush(queue, (dist, new))
        return distances[destination]
    
    cost = dijkstra(s, a) + dijkstra(s,b)
    for i in range(1, n+1):
        if s != i:
            cost = min(cost, dijkstra(s,i) + dijkstra(i,a) + dijkstra(i,b))
    
    return cost