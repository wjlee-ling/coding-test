import re
def solution(s):
    answer = s
    # while m:= re.search(r'\b[a-z][a-zA-Z0-9]*', answer):
    #     m = m.group()
    #     print(m)
    #     answer = re.sub('\b'+m, m.capitalize(), answer)
    ls = []
    for token in answer.split(' '):
        ls.append(token.capitalize())
    answer = ' '.join(ls)
    return answer