def solution(relation):
    # 칼럼 아이템들이 겹칠수도?
    def validate_key(combn_ls, candidate_keys=[]):
        from collections import defaultdict
        for indices in combn_ls:
            info = defaultdict(int)
            
            minimality_check=False
            for old_key in candidate_keys:
                if set(old_key) & set(indices) == set(old_key):
                    minimality_check = True
                    break
            if minimality_check == True:
                continue
            
            for row in relation:
                new_key = []
                for ind in indices:
                    new_key.append(row[ind])
                new_key = '_'.join(new_key)
                
                if info[new_key] == 0: # 새로운 키
                    info[new_key] = 1
                elif info[new_key] == 1: # 유일성 체크
                    break
                    
            if len(info) == len(relation):
                # 중복없음
                
                candidate_keys.append(indices)
        return candidate_keys
        
    from itertools import combinations
    n_features = len(relation[0])
    candidate_keys = []
    
    for n in range(1, n_features+1):
        ls  = list(combinations(range(n_features), n))
        candidate_keys = validate_key(ls, candidate_keys)
        
    answer = len(candidate_keys)
    return answer
    
    
    """ 기존 풀이 : success
    from itertools import combinations as c
    import re
    n_col = len(relation[0])
    indices_ls = []
    for n in range(1, n_col+1):
        combns = list(c(range(n_col), n))
        indices_ls.extend(combns)
        
    keys = []
    for rel in relation:
        for indices in indices_ls.copy():
            key = ''
            for ind in indices:
                key += f'<{ind}>'+rel[ind] # e.g. "<0>100<1>ryan<2>music<3>2" / "<3>2"

            # 유일성 체크
            if key in keys:
                if indices in indices_ls:
                    indices_ls.remove(indices) 
                continue
            keys.append(key)

    # 최소성
    to_remove = []
    for i in range(len(indices_ls)-1):
        for j in range(i+1, len(indices_ls)):
            if set(indices_ls[i]).intersection(set(indices_ls[j])) == set(indices_ls[i]):
                if j not in to_remove:
                    to_remove.append(j)
                    
    answers = [ind for ind in range(len(indices_ls)) if ind not in to_remove]
    return len(answers)"""