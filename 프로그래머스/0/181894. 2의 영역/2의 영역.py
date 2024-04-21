def solution(arr):
    answer = []
    for index,value in enumerate(arr):
        if value == 2:
            answer.append(index)
    if not answer:
        return[-1]
    start = answer[0]
    end = answer[-1]
    return arr[start:end+1]