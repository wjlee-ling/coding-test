def solution(n, wires):
    '''
    3rd try: tree끼리 union할 때 자식 노드들은 새 root값으로 업데이트 시켜줘야 함 예시 (1,7) (3,4) (3,7) 시 4번은 1로 업데이트 되지 않고 3으로 남음. (예시3)
    '''
    
    #wires = sorted(wires, key=lambda x: (x[0], x[1])) 

    class Node():
        def __init__(self, idx):
            self.idx = idx # unchanged
            self.parent = idx
            self.children = [] # container of nodes
            self.count = 1
            
        def update_parent(self):
            for child in self.children:
                if child.parent != self.parent:
                    child.parent = self.parent
                    child.update_parent()
        def __repr__(self):
            return str(self.parent)
        
    class UnionFind():
        def __init__(self, n_nodes):
            self.tree = [Node(idx) for idx in range(n_nodes+1)]
            
            
        def find_parent(self, idx):
            if self.tree[idx].parent != idx:
                self.tree[idx].parent = self.find_parent(self.tree[idx].parent)
            return self.tree[idx].parent
        
        def union(self, idx_x, idx_y):
            parent_x = self.find_parent(idx_x)
            parent_y = self.find_parent(idx_y)
            
            if parent_x < parent_y:
                self.tree[parent_y].parent = parent_x
                self.tree[parent_y].update_parent()
                if self.tree[parent_y] not in self.tree[parent_x].children:
                    self.tree[parent_x].children.append(self.tree[parent_y])
            else:
                self.tree[parent_x].parent = parent_y
                self.tree[parent_x].update_parent()
                if self.tree[parent_x] not in self.tree[parent_y].children:
                    self.tree[parent_y].children.append(self.tree[parent_x])
                
    diff_ls = []
    for i in range(n-1):
        uf = UnionFind(n)
        for j in range(n-1):
            if i == j:
                continue
            v1, v2 = wires[j]
            uf.union(v1, v2)
        
        counts = [node.parent for node in uf.tree][1:]
        count1 = counts.count(set(counts).pop())
        count2 = n-count1
        diff_ls.append(abs(count1-count2))
        
    answer = min(diff_ls)
    
    
    """## solution 1 -> successful but takes too long
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
        answer = min(answer, abs(count1-count2))"""
    
    """# solution2: union-find -> failure
    
    def find(x, parents):
        # x가 속한 tree의 root 찾기
        route = []
        if parents[x] != x:
            route.append(parents[x]) # 지나간 (루트가 아닌) 부모 노드의 index 저장
            return find(parents[x], parents)
        for idx in route:
            # (루트가 아닌) 부모 노드들의 값을 local root node -> global root node로 업데이트 
            parents[idx] = x 
        return x
    
    def union(x, y, parents):
        x_root = find(x, parents)
        y_root = find(y, parents)
        
        if x_root < y_root:
            parents[y_root] = x_root
        else:
            parents[x_root] = y_root

        return parents
    
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
        answer = min(answer, diff)
        
    return answer"""
    
    return answer