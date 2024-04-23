def solution(n):
    if n<1:
        return 0
    fact = 1
    i =1
    while True:
        fact *= i
        if fact >n:
            break
        i +=1
    return i -1