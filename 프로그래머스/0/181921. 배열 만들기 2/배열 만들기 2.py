def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        s_num = str(i)
        if set(s_num).issubset({'0','5'}):
            answer.append(i)
    if not answer:
        return [-1]
    return answer