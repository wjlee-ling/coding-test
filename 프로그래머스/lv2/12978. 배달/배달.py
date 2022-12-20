def solution(N, road, K):
    import heapq  # 우선순위 큐 구현을 위함
    from collections import defaultdict
    graph = defaultdict(dict)
    for x,y,d in road:
        if y not in graph[x]:
            graph[x].update({y:d})
            graph[y].update({x:d})
        else:
            graph[x][y] = min(d, graph[x][y])
            graph[y][x] = min(d, graph[y][x])
    
    def dijkstra(graph, start):
        inf = float('inf')
        distances = {node: inf for node in graph}  # start로 부터의 거리 값을 저장하기 위함
        distances[start] = 0  # 시작 값은 0이어야 함
        queue = []
        heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

        while queue:  # queue에 남아 있는 노드가 없으면 끝
            current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

            if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
                continue

            for new_destination, new_distance in graph[current_destination].items():
                distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
                if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                    distances[new_destination] = distance
                    heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

        return distances
    distances = dijkstra(graph, 1)
    return len([n for n, d in distances.items() if d <=K])

#     # first try -> success
#     from collections import defaultdict
#     roads = defaultdict(list)
#     for a,b,dist in road:
#         roads[a].append((b,dist))
#         roads[b].append((a,dist))
    
#     heap = [1]
#     dist_ls = [float("inf")]*(N+1)
#     seen = [0]*(N+1)
#     dist_ls[1] = 0
#     seen[1] = 1
#     while heap:
#         curr = heap.pop(0) #curr = heapq.heappop(heap)
#         if seen[curr] == 1:
#             for next_, dist in roads[curr]:
#                 if dist_ls[next_] > dist_ls[curr] + dist:
#                     dist_ls[next_] = dist_ls[curr] + dist
#                     heap.append(next_)#heapq.heappush(heap, next_)
#                     seen[next_] = 1
            
#     return len([dist for dist in dist_ls if dist <=K])