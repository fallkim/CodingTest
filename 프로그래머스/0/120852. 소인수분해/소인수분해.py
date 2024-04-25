def solution(n):
    factors = []
    divisor = 2  # 2부터 시작
    
    while n > 1:
        if n % divisor == 0:
            if divisor not in factors:
                factors.append(divisor)
            n//= divisor
        else:
            divisor += 1
    return factors