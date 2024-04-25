def solution(array):
    answer = 0
    for i in array:
        num= str(i)
        answer += num.count('7')
    return answer