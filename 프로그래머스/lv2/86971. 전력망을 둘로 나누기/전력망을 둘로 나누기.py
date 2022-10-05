def solution(n, wires):
    
    ## solution 1
    from collections import defaultdict
    
    def make_tree(wires):
        connected = defaultdict(list)
        for pair in wires:
            connected[pair[0]].append(pair[1])
            connected[pair[1]].append(pair[0])
        return connected
        
    # search and count nodes of sub-trees
    def search(tree, start):
        history, stack = [], [start]
        count = 1
        while stack:
            curr = stack.pop()
            count+=1
            for node in tree[curr]:
                if (curr, node) in history or (node, curr) in history:
                    continue
                stack.append(node)
                history.extend([(curr,node), (node, curr)])
        return count
    
    answer = 10000
    
    for i in range(len(wires)):
        v1, v2 = wires[i]
        connected = make_tree(wires[:i] + wires[i+1:] )
        count1 = search(connected, v1)
        count2 = search(connected, v2)
        answer = min(answer, abs(count1-count2))

    """## solution 2: using Union-find
    
    def find(x, parents):
        # x가 속한 tree의 root 찾기
        if parents[x] != x:
            return find(parents[x], parents)
        return x
    
    def union(x, y, parents):
        x_root = find(x, parents)
        y_root = find(y, parents)
        
        if x_root < y_root:
            parents[y_root] = x_root
        else:
            parents[x_root] = y_root
        return parents
    
    # wires가 sort되지 않았을 때 대비
    wires = sorted(wires, key=lambda x: (x[0], x[1]))
    
    answer = 10000
    for i in range(n-1):
        # edge는 n-1개라는 게 조건
        # i 번째 edge는 연결 안함
        
        # parent 초기화 -> {현재 노드: root 노드}
        parents = {num:num for num in range(1, n+1)} 
        for j, (v1, v2) in enumerate(wires):
            if i == j:
                continue
            parents = union(v1, v2, parents)
            
        roots = list(parents.values())
        roots_set = set(roots)
        diff = abs(roots.count(roots_set.pop()) - roots.count(roots_set.pop()))
        answer = min(answer, diff)"""
        
    return answer