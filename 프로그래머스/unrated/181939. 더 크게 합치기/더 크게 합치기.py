def solution(a, b):
    i = str(a)+str(b)
    j = str(b)+str(a)
    if i> j:
        answer = int(i)
    elif i == j:
        answer = int(i)
    else:
        answer = int(j)
        
    return answer