def kify(n, k):
    q, r = divmod(n,k) 
    result = str(r) 
    while q >= k : 
        q, r = divmod(q, k) 
        result = str(r) + result 
    result = str(q) + result
    return result

"""def get_prime_numbers(max_n):
    arr = [0, 0] + [1] * (max_n-1)
    max_parent_n = int(max_n **0.5)
    for n in range(2, max_parent_n+1):
        # 2부터 search
        if arr[n] ==1:
            for multiplied in range(2*n, max_n+1, n):
                arr[multiplied] = 0
    prime_numbers = [k for k,v in enumerate(arr) if v == 1] # 0 포함 안됨
    return prime_numbers"""

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
    
def solution(n, k):
    '''
    1. k 진수로 바꾸기... 뭐였지
    2. string , re 라이브러리 사용? (사용하면 greedy search)
    3. 소수에는 0이 없어야 함!!
    4. 119 같은 소수 찾으려면 소수 찾는 알고리즘도 짜야 하는지.. 그러면 맥시멈 어디까지 search?
    n_in_k 를 쓰면 너무 큼
    '''
    import re
    
    answer = 0
    n_in_k = kify(n, k) # string
    token_ls = n_in_k.split('0')
    
    for token in token_ls:
        # 이 token 에는 0 이 포함안됨
        if token == '':
            continue
        if is_prime(int(token)) :
            # token == 
            answer += 1
            
    return answer