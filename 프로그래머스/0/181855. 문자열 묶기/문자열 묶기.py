def solution(strArr):
    answer = {}
    for i in strArr:
        length = len(i)
        if length in answer :
            answer[length] += 1
        else:
            answer[length] =1
    return max(answer.values())