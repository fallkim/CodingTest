def solution(a, b):
    answer = 0
    j = 2*a*b
    i = str(a)+str(b)
    if int(i)>j:
        answer = int(i)
    elif i ==j:
        answer = int(i)
    else:
        answer = int(j)
    return answer