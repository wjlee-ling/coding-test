def solution(n, works):
    '''1st try -> failed efficiency test
    reduce maximum value by 1 
    
    if n >= sum(works):
        # no need to work until late
        return 0
    while n:
        maxind = works.index(max(works))
        works[maxind] -= 1
        n -=1
    answer = [x**2 for x in works]
    answer = sum(answer)
    '''
    # 2nd
    from collections import defaultdict
    if n >= sum(works):
        return 0
    c = defaultdict(int)
    max_time = max(works)
    for work in set(works):
        # {time: # of time}
        c[work] = works.count(work)
    
    while n:
        c[max_time] -= 1
        if max_time-1 > 0:
            c[max_time-1] +=1
        if c[max_time] == 0:
            max_time -=1
        n -= 1
    
    answer = sum([k**2 * v for k,v in c.items()])
    return answer