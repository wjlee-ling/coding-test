def solution(distance, scope, times):
    '''
    2nd try: sorting 추가
    '''
    from itertools import repeat
    answer = 0 # distance

    def shift(time, ts=1):
        # 근무자 한명의 timestep별 근무 여부 -> 근무 중이면 1 리턴
        # ts 는 1부터
        schedule = list(repeat(1, time[0])) + list(repeat(0, time[1])) # 일하는 시간 1, 아니면 0
        unit = len(schedule) # working second + break 
        r = ts % unit 
        return schedule[r-1]

    # sorting
    scope_sorted = sorted(scope, key=lambda x: x[0])
    indices = []
    for s in scope_sorted:
        ind = scope.index(s)
        indices.append(ind)
    times_sorted = [times[ind] for ind in indices]
    
    ts = 1
    ward = scope_sorted[0] # 경비지역
    while True:
        # 미리 갈 수 있는지 보기
        if ts < min(ward):
            # 경비 없는 지역
            pass
        else:
            time = times_sorted[0] # 현재/다음 근무자의 일/휴식 비율
            is_shift = shift(time, ts)
            if is_shift:
                # 근무 중
                return ts
            elif ts == max(ward):
                # 현재 있는 근무지 마지막 칸에 도착
                scope_sorted.pop(0)
                times_sorted.pop(0)
                ward = scope_sorted[0] # update next_ward
                
        if ts == distance:
            return ts
        # 다음 칸에 근무 중이 아니라 움직이기
        ts+=1
        
    return ts
    
    """
    '''1st try:
    각 timestep별 근무자 시간표를 바탕으로 걸리는지 확인
    scope/times: num-1 !!
    '''
    from itertools import repeat
    answer = 0 # distance

    def shift(time, ts=1):
        # 근무자 한명의 timestep별 근무 여부 -> 근무 중이면 1 리턴
        # ts 는 1부터
        schedule = list(repeat(1, time[0])) + list(repeat(0, time[1])) # 일하는 시간 1, 아니면 0
        unit = len(schedule) # working second + break 
        r = ts % unit 
        return schedule[r-1]

    
    ts = 1
    ward = scope[0] # 경비지역
    while True:
        # 미리 갈 수 있는지 보기
        if ts < min(ward):
            # 경비 없는 지역
            pass
        else:
            time = times[0] # 현재/다음 근무자의 일/휴식 비율
            is_shift = shift(time, ts)
            if is_shift:
                # 근무 중
                return ts
            elif ts == max(ward):
                # 현재 있는 근무지 마지막 칸에 도착
                scope.pop(0)
                times.pop(0)
                ward = scope[0] # update next_ward
                
        if ts == distance:
            return ts
        # 다음 칸에 근무 중이 아니라 움직이기
        ts+=1
        
    return ts"""