def solution(arr, queries):
    for i,j,k in queries:
        for n in range(i,j+1):
            if n %k == 0:
                arr[n] += 1
    return arr