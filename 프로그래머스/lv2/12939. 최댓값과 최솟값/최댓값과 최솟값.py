def solution(s):
    answer = ''
    ls = sorted(map(int, s.split()))
    answer = str(min(ls)) + ' '+ str(max(ls))    
    return answer