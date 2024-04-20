def solution(arr):
    if len(arr) & (len(arr)-1) ==0:
        return arr
    answer =1
    while answer < len(arr):
        answer *= 2
    result = answer -len(arr)
    arr.extend([0]*result)
    return arr