def solution(numlist, n):
    answer = [(abs(x-n),-x,x) for x in numlist]
    answer.sort()
    
    result = [x[2] for x in answer]
    return result