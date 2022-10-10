def solution(n,a,b):
    from math import log
    answer = 0
    a,b = min(a,b), max(a,b)
    base = 0
    while n>1:
        n = n//2 
        if a <= n+base and b>n+base:
            answer = log(n,2) +1
            break
        elif a > n+base: # 둘다 경계선보다 오른쪽
            base += n
    return answer