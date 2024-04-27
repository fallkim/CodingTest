import math
def solution(a, b):
    answer = math.gcd(a,b)
    a //= answer
    b //= answer
    
    for i in [2,5]:
        while b % i == 0:
            b //=i
    if b ==1:
        return 1
    else:
        return 2