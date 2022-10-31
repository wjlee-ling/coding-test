def solution(str1, str2):
   
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    letters ='abcdefghijklmnopqrstuvwxyz'
    combn1 = [str1[i]+str1[i+1] for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()]
    combn2 = [str2[i]+str2[i+1] for i in range(len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()]
    total = combn1+combn2
    inter, union = 0, 0
    for unit in set(total):
        c1, c2 = combn1.count(unit), combn2.count(unit)
        union+=max(c1,c2)
        inter+=min(c1,c2)
    answer = int(inter/union *65536) if union * inter > 0 else 0
    if total == []: answer = 65536
    
    return answer