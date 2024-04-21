def solutions(arr):
    answer = []
    for i in arr:
        if i >= 50 and i% 2 == 0 :
            answer.append(i/2)
        elif i<50 and i %2 != 0:
            answer.append(i*2+1)
        else:
            answer.append(i)
    return answer

def solution(arr):
    n=0
    while True:
        answer = solutions(arr)
        if answer == arr:
            return n
        arr = answer
        n += 1
    return n
