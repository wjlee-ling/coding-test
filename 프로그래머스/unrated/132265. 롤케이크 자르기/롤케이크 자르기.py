def solution(topping):
    from collections import Counter
    left = Counter()
    right = Counter(topping)
    answer = 0
    for t in topping:
        left.update({t:1})
        right.update({t:-1})
        if right[t] == 0: del right[t]
        if len(right) == len(left):
            answer += 1
        
    return answer