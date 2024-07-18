def solution(x):
    hassa = sum(int(i) for i in str(x))
    if x % hassa == 0 :
        return True
    else:
        return False