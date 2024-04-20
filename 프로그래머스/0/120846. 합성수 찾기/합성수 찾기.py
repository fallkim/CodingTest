def solution(n):
    if n < 2:
        return 0
    count = 0
    
    for i in range(2, n+1):
        answer = False
        for j in range(2,int(i**0.5) +1):
            if i % j ==0:
                answer = True
                break
        if answer:
            count += 1
    return count