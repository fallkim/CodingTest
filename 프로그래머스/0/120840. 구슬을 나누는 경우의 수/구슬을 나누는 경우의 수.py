def fact(n):
    if n ==0:
        return 1
    else:
        return n *fact(n-1)
    
def solution(balls, share):
    return fact(balls) //(fact(share) * fact(balls-share))