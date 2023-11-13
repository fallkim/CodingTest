def solution(arr, queries):
    answer=[]
    for query in queries:
        s,e,k = query
        a = [num for num in arr[s:e+1] if num> k]
        if a:
            answer.append(min(a))
        else:
            answer.append(-1)
    return answer