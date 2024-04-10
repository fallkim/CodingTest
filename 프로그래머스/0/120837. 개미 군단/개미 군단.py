def solution(hp):
    answer = 0
    x=5
    y=3
    z=1
    
    answer += hp //x
    hp %= x
    
    answer += hp//y
    hp %=y
    
    answer += hp//z
    return answer