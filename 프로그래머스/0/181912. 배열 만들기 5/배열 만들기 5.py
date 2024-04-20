def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        if len(i) >= s+1:
            num = int(i[s:s+l])
            if num > k:
                answer.append(num)
    return answer