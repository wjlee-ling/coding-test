def solution(enroll, referral, seller, amount):
    '''
    1st try: 재귀 함수로 구현
    마지막 소수점 절사 관련 문제 -> 질문하기 답변 참고함
    '''
    from collections import defaultdict
    answer = [] 
    account = defaultdict(int)
    get_parent = {ch:par for par, ch in zip(referral, enroll)}
    
    def share(profit, person):
        '''
        수익 90 % 먹고 10% 추천인에게 넘기는 함수 (if not center and profit > 9) 
        첫 profit: 판매한 칫솔 * 개수 // 그 다음 profit: 첫 profit의 0.9
        '''
        parent = get_parent[person]
        to_share = profit // 10
        account[person] += profit -to_share
        if parent != '-' and to_share >= 1:
            return share(to_share, parent)
    for s, a in zip(seller, amount):
        profit = a * 100
        share(profit, s)
    for person in enroll:
        saved = account[person]
        answer.append(saved)
    return answer