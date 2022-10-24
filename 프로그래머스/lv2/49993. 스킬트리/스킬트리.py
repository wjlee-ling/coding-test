def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        ind = -1 # should be ascending over the chars of skill 
        flag = False
        for char in skill:
            if char in tree:
                char_ind = tree.index(char)
            else:
                # tree에 없는 char이기 때문에 최대 인덱스값으로 설정
                char_ind = 26 # max_len
            ind = max(ind, char_ind)
            if ind != char_ind:
                flag = True
                break
        if not flag:
            print(tree)
            answer += 1
    return answer