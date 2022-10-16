def solution(cards):
    from functools import reduce
    answer = 0
    # d 만들기    
    d = {i:[i] for i in range(1, len(cards)+1)}
    for card in cards:
        start_card = card
        while cards[card-1] != card :
            if cards[card-1] in d[start_card]:
                break
            d[start_card].append(cards[card-1])
            card = cards[card-1]
        d[start_card].sort()
    ls = []
    for v in d.values():
        if v not in ls:
            ls.append(v)
    ls = sorted(ls, key=len)
    ls = [len(x) for x in ls]
    try:
        answer = ls[-1] * ls[-2]
    except:
        answer = 0
    return answer