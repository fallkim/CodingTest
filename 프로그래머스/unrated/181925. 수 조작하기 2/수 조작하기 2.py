def solution(numLog):
    answer = ''
    for j in range(1, len(numLog)):
        i = numLog[j] - numLog[j-1]
        if i == 1:
            answer += 'w'
        elif i == -1:
            answer += 's'
        elif i == 10:
            answer += 'd'
        elif i == -10 :
            answer += 'a'
    return answer