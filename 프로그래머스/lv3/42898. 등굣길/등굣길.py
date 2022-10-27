def solution(m, n, puddles):
    answer = 0
    graph = [[0] *m for _ in range(n)]
    for i in range(n):
        for j in range(m) :
            if (i,j) == (0,0):
                graph[i][j] = 1
            if [j+1, i+1] in puddles:
                continue
            # downward
            if i +1 < n and [j+1, i+2] not in puddles:
                graph[i+1][j] += graph[i][j]
            # to the right
            if j+1 < m and [j+2, i+1] not in puddles:
                graph[i][j+1] += graph[i][j]
    print(graph)
    answer = graph[n-1][m-1]
    return answer % 1000000007