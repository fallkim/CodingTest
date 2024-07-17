def solution(s):
    alpha = s.lower()
    p = alpha.count('p')
    y = alpha.count('y')
    if p!=y:
        return False
    else:
        return True