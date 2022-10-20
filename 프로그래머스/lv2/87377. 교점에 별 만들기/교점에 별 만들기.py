def solution(line):
    
    def cross_at(line1, line2):
        '''교점의 x,y 좌표'''
        a, b, e = line1
        c, d, f = line2
        denom = (a*d - b*c)
        if denom == 0:
            # 서로 접점이 없으면 패스
            return False
        x, y = (b*f - e*d) / denom , (e*c-a*f) /denom
        if int(x) != x or int(y) != y:
            # 정수가 아니면 패스
            return False
        return (int(x),int(y))
    
    def draw(coordinates):
        x_min, x_max, y_min, y_max = float("inf"), -float("inf"), float("inf"), -float("inf")
        for coord in coordinates:
            x_min, x_max = min(x_min, coord[0]), max(x_max, coord[0])
            y_min, y_max = min(y_min, coord[1]), max(y_max, coord[1])
        
        palette = [["."] * (x_max-x_min+1) for _ in range(y_max-y_min+1)]
        for coord in coordinates:
            x, y = coord
            dist_x, dist_y = x-x_min, y_max-y
            palette[dist_y][dist_x] = "*" 

        return palette
        
        
    from itertools  import combinations
    combns = combinations(range(len(line)), 2)
    answer = []
    for l1, l2 in combns:
        coord = cross_at(line[l1], line[l2])
        if not coord:
            # 교점이 없으면
            continue
        answer.append(coord)
    answer = draw(answer)        
    answer = [''.join(row) for row in answer]
        
    return answer
