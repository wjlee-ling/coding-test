def solution(n, t, m, p):
    ''' 1st try:
    1. n진수 변환
    2. 숫자대로 변환
    '''
    from itertools import cycle
    
    def convert(num):
        int2str = {10: 'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        str2int = {v:k for k,v in int2str.items()}
        new = ''
        if num // n == 0:
            return str(num) if num not in int2str else int2str[num]
        
        while num // n:
            q, r = divmod(num, n)
            q, r = map(lambda x: int2str[x] if x in int2str else x, (q,r))
            new = str(r) + new
            num = str2int[q] if q in str2int else q
            
        return str(q) + new

    turns = cycle([1 if i == p-1 else 0 for i in range(m)]) # 튜브의 순서에만 1, 나머지 0
    
    num10, answer = 0, ''
    num = convert(num10)

    for turn in turns:
        current = num[0] # 현재 외쳐야 하는 숫자
        num = num[1:] # update 
        if num == '': 
            # 새 숫자로 초기화
            num10+=1
            num = convert(num10)
        if turn:
            answer += current
        if len(answer) == t:
            break
    
    return answer