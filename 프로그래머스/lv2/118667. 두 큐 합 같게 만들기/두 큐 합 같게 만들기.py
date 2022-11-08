def solution(queue1, queue2):
    """
    1st try: queue 하나가 sum/2 
    """
    from collections import deque
    answer = 0
    target = (sum(queue1) + sum(queue2)) / 2
    if target != int(target):
        return -1
    else:
        target = int(target)
    q1, q2 = deque(queue1), deque(queue2)
    s = sum(q1)
    limit = len(q1) + len(q2) * 2
    i = 0
    while s != target:
        if s < target:
            new = q2.popleft()
            q1.append(new)
            s += new
        elif s > target:
            old = q1.popleft()
            q2.append(old)
            s -= old
        answer += 1    
        if s == target:
            break
        if  len(q1) == 0:
            return -1
        i+=1
        if i == limit:
            return -1
    return answer