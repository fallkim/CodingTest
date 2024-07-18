def solution(arr):
    answer = 0
    for i in arr :
        answer += int(i)
        a = answer / len(arr)
    return a