'''2nd try:
1. distancing : if satisfied -> True


'''
def distancing(start, graph):
    x_moves, y_moves = [1,-1,0,0], [0,0,1,-1]
    stack = [(start[0], start[1])]
    while stack:
        cx, cy = stack.pop()
        graph[cx][cy] = 'X' # 방문처리
        for dx, dy in zip(x_moves, y_moves):
            nx, ny = cx+dx, cy+dy
        
            if nx <0 or nx >4 or ny <0 or ny>4:
                continue
            if graph[nx][ny] == 'X':
                # wall
                continue
            if abs(nx-start[0]) + abs(ny-start[1]) > 2:
                # over the minimum manhatten dist
                continue
            if graph[nx][ny] == 'O':
                stack.append((nx, ny)) 
                graph[nx][ny] = 'X' # 방문처리
            if graph[nx][ny] == 'P':
                return False
    return True

def solution(places):
    answer = []
    for room in places:
        room = [list(row) for row in room]
        results = []
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    result = distancing((i,j), room)
                    results.append(result)
        if all(results):
            answer.append(1)
        else:
            answer.append(0)
    return answer         
"""from collections import deque


def vicinity(point, graph):
    origin = point
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    queue = deque([point])
    answer = 1
    while queue:
        curr = queue.popleft()
        cx, cy = curr[0], curr[1]
        for x,y in zip(dx,dy):
            nx, ny = cx+x, cy+y
            if abs(nx-origin[0]) + abs(ny-origin[1])  > 2:
                continue
            if nx <0 or nx >=5 or ny <0 or ny >=5:
                continue
            
            new = graph[nx][ny]
            if new == 'P':
                answer = 0
                break
            if new == 'O':
                queue.append([nx,ny])
                graph[cx] = graph[cx][:cy] + "X" + graph[cx][cy+1:]

    return answer

def solution(places):
    answer = []
    
    for place in places:
        ls = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    result = vicinity([i,j], place)
                    ls.append(result)
        answer.append(int(all(ls)))
    return answer"""